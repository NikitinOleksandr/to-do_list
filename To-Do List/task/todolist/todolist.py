from datetime import datetime, timedelta

from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///todo.db?check_same_thread=False')

Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

menu = """
1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit
"""

weekdays = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
]


def today_tasks():
    today = datetime.today().date()
    rows = session.query(Table).filter(Table.deadline == today).all()
    print("Today", today.day, today.strftime('%b'))
    if not rows:
        print('Nothing to do!')
    else:
        for row in rows:
            if row.deadline == today:
                print(row.task)


def week_tasks():
    today = datetime.today().date()
    for day in weekdays:
        task_number = 1
        rows = session.query(Table).filter(Table.deadline == today).all()
        print(weekdays[today.weekday()], today.day, today.strftime('%b') + ":")
        if not rows:
            print('Nothing to do!')
        else:
            for row in rows:
                if row.deadline == today:
                    print(str(task_number) + ". " + row.task)
                    task_number += 1
        print()

        today += timedelta(days=1)


def all_tasks():
    today = datetime.today().date()
    rows = session.query(Table).all()
    task_number = 1
    print("All tasks:")
    for row in rows:
        print(
            str(task_number) + ". " + row.task + ". " + str(row.deadline.day) + " " + str(row.deadline.strftime('%b')))
        task_number += 1


def add_task():
    task = input('Enter task\n')
    deadline = datetime.strptime(input('Enter deadline\n'), '%Y-%m-%d')
    new_row = Table(task=task, deadline=deadline)
    session.add(new_row)
    session.commit()
    print('The task has been added!\n')


def missed_tasks():
    today = datetime.today().date()
    rows = session.query(Table).order_by(Table.deadline).filter(Table.deadline < today).all()
    task_number = 1
    print("Missed tasks:")
    if not rows:
        print('Nothing to do!')
    else:
        for row in rows:
            print(str(task_number) + ". " + row.task + ". " + str(row.deadline.day) + " " + str(
                row.deadline.strftime('%b')))
            task_number += 1


def delete_task():
    rows = session.query(Table).order_by(Table.deadline).all()
    task_number = 1
    print("Chose the number of the task you want to delete:")
    if not rows:
        print("Nothing to delete")
    else:
        for row in rows:
            print(str(task_number) + ". " + row.task + ". " + str(row.deadline.day) + " " + str(
                row.deadline.strftime('%b')))
            task_number += 1
    specific_row = rows[int(input())]
    session.delete(specific_row)
    session.commit()
    print("The task has been deleted!")


while True:
    print(menu)
    command = input()

    if command == '1':
        today_tasks()
        continue
    elif command == '2':
        week_tasks()
        continue
    elif command == '3':
        all_tasks()
        continue
    elif command == '4':
        missed_tasks()
        continue
    elif command == "5":
        add_task()
        continue
    elif command == '6':
        delete_task()
        continue
    elif command == '0':
        print("\nBye!")
        break
