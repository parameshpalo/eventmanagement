from fastapi import APIRouter, Body, Depends, HTTPException
from db import get_db
import models
import schemas
from oauth2 import get_current_user

router=APIRouter(tags=['Events'])

@router.post('/event')
def create_event(new_event: schemas.CreateEvent, db = Depends(get_db), current_user = Depends(get_current_user)):
  new_event=models.Event(event_organiser=current_user.user_id,**new_event.dict())
  db.add(new_event)
  db.commit()
  db.refresh(new_event)
  return new_event

@router.get('/events')
def get_all_events(db = Depends(get_db),current_user = Depends(get_current_user)):
  events=db.query(models.Event).all()
  if not events:
     raise HTTPException(status_code=404,detail="No current events found")
  return events

@router.get('/events/{id}')
def get_events_by_id(id:int,db = Depends(get_db),current_user = Depends(get_current_user)):
  event=db.query(models.Event).filter(models.Event.event_id==id).first()
  if not event:
    raise HTTPException(status_code=404,detail="event not found")
  return event
  

@router.put('/events/{id}')
def update_events_by_id(id:int , updated_event: schemas.UpdateEvent,db = Depends(get_db),current_user = Depends(get_current_user)):
  event_query = db.query(models.Event).filter(models.Event.event_id == id)
  event = event_query.first()
  if not event:
    raise HTTPException(status_code=404,detail="event not found")
  if event.event_organiser != current_user.user_id:
        raise HTTPException(status_code=403,detail="Not authorized to perform requested action")
  update_data = updated_event.dict(exclude_unset=True)
  event_query.update(update_data)
  db.commit()
  return event_query.first()


@router.delete('/events/{id}')
def delete_events_by_id(id : int,db = Depends(get_db),current_user = Depends(get_current_user)):
  event_query = db.query(models.Event).filter(models.Event.event_id == id)
  event = event_query.first()
  if event.event_organiser != current_user.user_id:
        raise HTTPException(status_code=403,detail="Not authorized to perform requested action")
  if event is None:
    raise HTTPException(status_code=404,detail=f"Event with id {id} does not exist")
  event_query.delete()
  db.commit()
  return {"detail": f"Event with id {id} deleted successfully"}