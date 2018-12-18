from rq import Queue
from worker import conn
from send_friend_requests import working_process

q = Queue(connection=conn)

result = q.enqueue(working_process, 'http://heroku.com')
