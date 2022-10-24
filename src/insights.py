from src.jobs import read


def get_unique_job_types(path: str) -> list:
    all_jobs = read(path)
    unique_job = set()
    for job in all_jobs:
        unique_job.add(job["job_type"])

    return unique_job


def filter_by_job_type(jobs: dict, job_type: str) -> list:
    filter_jobs = []
    for job in jobs:
        if job['job_type'] == job_type:
            filter_jobs.append(job)
    return filter_jobs


def get_unique_industries(path: str) -> list:
    all_jobs = read(path)
    industries = set()
    for job in all_jobs:
        industries.add(job["industry"])
        industries = industries - {""}

    return industries


def filter_by_industry(jobs: dict, industry: str) -> list:
    filter_industries = []
    for job in jobs:
        if job['industry'] == industry:
            filter_industries.append(job)
    return filter_industries


def get_max_salary(path: str) -> int:
    all_jobs = read(path)
    max_salary = []
    for job in all_jobs:
        try:
            max_salary.append(int(job["max_salary"]))
        except ValueError:
            continue
    return max(max_salary)


def get_min_salary(path: str) -> int:
    all_jobs = read(path)
    min_salary = []
    for job in all_jobs:
        try:
            min_salary.append(int(job["min_salary"]))
        except ValueError:
            continue
    return min(min_salary)


def matches_salary_range(job: dict, salary: int) -> bool:
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("'min_salary' or 'max_salary' doesn't exists.")
    elif (type(job["min_salary"]) != int) or (type(job["max_salary"]) != int):
        raise ValueError("'min_salary' or 'max_salary' aren't valid integers.")
    elif (type(salary) != int) or (type(job["max_salary"]) != int):
        raise ValueError("salary isn't valid integer.")
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError("'min_salary' is greather than 'max_salary'.")

    check_salary = (
        job["min_salary"] <= salary <= job["max_salary"]
    )
    return check_salary


def filter_by_salary_range(jobs: dict, salary: int) -> list:
    filter_salary = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filter_salary.append(job)
        except ValueError:
            continue
    return filter_salary
