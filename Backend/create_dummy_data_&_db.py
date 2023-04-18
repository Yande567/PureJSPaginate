from datetime import date, timedelta
from faker import Faker
from sqlalchemy import create_engine, Column, Integer, String, Date, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# create a SQLAlchemy engine to connect to the SQLite database
engine = create_engine('sqlite:///db.sqlite3', echo=True)

# create a session factory
Session = sessionmaker(bind=engine)

# create a declarative base class for the ORM
Base = declarative_base()

# Create Employee class
class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    position = Column(String(50))
    dob = Column(Date)
    age = Column(Integer)
    start_date = Column(Date)
    office = Column(String(50))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __repr__(self):
        return f"Employee(name='{self.first_name} {self.last_name}', position='{self.position}', "

# Custom faker provider for generating job titles
class CustomJobProvider:
    def __init__(self, faker):
        self.faker = faker

    def job(self):
        job_titles = [
            "Software Engineer", "Web Developer", "Frontend Developer",
            "Backend Developer", "Full Stack Developer", "DevOps Engineer",
            "Data Scientist", "Data Analyst", "Quality Assurance Analyst",
            "UI/UX Designer", "Technical Writer", "Account Manager",
            "Accountant", "Bookkeeper", "Financial Analyst", "Financial Advisor",
            "Auditor", "Payroll Specialist", "Marketing Manager",
            "Marketing Coordinator", "Content Writer", "Copywriter",
            "Digital Marketing Specialist", "SEO Specialist", "Social Media Manager",
            "PR Specialist"
        ]
        return self.faker.random_element(job_titles)


# generate dummy data for the employees table
def generate_data(num_records=10):
    fake = Faker()
    fake.add_provider(CustomJobProvider)

    for i in range(num_records):
        first_name = fake.first_name()
        last_name = fake.last_name()
        position = fake.job()
        dob = fake.date_of_birth()
        age = (date.today() - dob) // timedelta(days=365.25)
        start_date = fake.date_between(start_date='-10y', end_date='today')
        office = fake.company()
        created_at = fake.date_time_between(start_date='-1y', end_date='now')
        updated_at = fake.date_time_between(start_date=created_at, end_date='now')

        employee = Employee(first_name=first_name, last_name=last_name, position=position, dob=dob, age=age,
                            start_date=start_date, office=office, created_at=created_at, updated_at=updated_at)

        # add the employee to the session and commit the transaction
        session = Session()
        session.add(employee)
        session.commit()


if __name__ == '__main__':
    # create the employees table in the database
    Base.metadata.create_all(engine)

    # generate 50 records of dummy data
    generate_data(50)
