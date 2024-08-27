from fastapi import FastAPI, HTTPException, Response 
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
import logging
import time

from app.db.MongoDBRepository import MongoDBRepository
from app.routes import sources
from app.routes import ingestor
from app.routes import inferer

from app.jobs import sync
import datetime

app = FastAPI(title="RagAPI",
              description="RAG API",
              summary="Summary ...",
              version="0.0.1",
              terms_of_service="someurls",
              contact={
                  "name":"Shailender Chohan",
                  "url": "https://www.linkedin.com/in/shailender/",
                  "email": "contact.ssc3@gmail.com"
                  },
              license_info={
                  "name": "MIT License",
                  "url": "http://www.opensource.org/licenses/mit"
              },
              _env_file=".env")


# configure logging
logging.basicConfig(
    format='%(asctime)s - %(process)s - %(name)s:%(lineno)d - %(levelname)s -'
    ' %(message)s',
    level=logging.INFO,
)
logger = logging.getLogger(__name__).setLevel(logging.DEBUG)


# add main routes
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/ping")
async def version(response: Response):
    return {"data": "Ok at " + datetime.datetime.now().strftime("%c")}    


@app.get("/pause-jobs")
async def stop_jobs(response: Response):
    if job:
        job.pause()
    else:
        raise HTTPException(500, "Job could not be paused")    

    return {"data": "Jobs paused " + job.id }    


@app.get("/resume-jobs")
async def start_jobs(response: Response):
    if job:
        job.resume()
    else:
        raise HTTPException(500, "Job could not be resumed")    

    return {"data": "Jobs resumed" }    



async def on_startup():
    print("Starting FastAPI")


async def on_shutdown():
    print("Shutting down")
    
# initialize the database
MongoDBRepository.initialize()

# add other routes
app.include_router(sources.router) 
app.include_router(ingestor.router) 
app.include_router(inferer.router) 

# Create the scheduler and add jobs
scheduler = AsyncIOScheduler()
job = scheduler.add_job(sync.run, IntervalTrigger(seconds=5), id="sync") 

# Run every 10 seconds
#scheduler.start()

print("starting scheduler " + time.strftime("%A, %d %b %Y %H:%M:%S"))
