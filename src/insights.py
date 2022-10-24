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


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
