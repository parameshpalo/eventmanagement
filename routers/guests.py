from fastapi import APIRouter, Depends, HTTPException
from db import get_db
import models
import schemas
from oauth2 import get_current_user

router=APIRouter(tags=['Guests'])


@router.post('/events/{id}/guests')
def add_guest_to_event(id:int , new_guest:schemas.GuestReg,db=Depends(get_db)):
  new_guest=models.Guest(event_id=id,**new_guest.dict())
  db.add(new_guest)
  db.commit()
  db.refresh(new_guest)
  return new_guest



@router.get('/events/{id}/guests')
def get_all_guests_of_a_event(id:int , db=Depends(get_db)):
  guests_query=db.query(models.Guest).filter(models.Event.event_id==id)
  guests=guests_query.all()
  if not guests:
    raise HTTPException(status_code=404,detail="no guest found")
  return guests
  



@router.delete('/events/{id}/guests/{guest_id}')
def remove_guest_from_event(event_id : int,guest_id:int , db=Depends(get_db),current_user = Depends(get_current_user)):
  guest_query=db.query(models.Guest).filter(models.Guest.guest_id==guest_id)
  guest = guest_query.first()
  if guest is None:
    raise HTTPException(status_code=404,detail=f"guest with id {id} does not exist")
  event_query=db.query(models.Event).filter(models.Event.event_id==event_id)
  event=event_query.first()
  if event.event_organiser != current_user.user_id:
        raise HTTPException(status_code=403,detail="Not authorized to perform requested action")
  guest_query.delete()
  db.commit()
  return {"detail": f"Guest with id {guest_id} deleted successfully"}