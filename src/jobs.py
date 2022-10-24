from functools import lru_cache
import csv


@lru_cache
def read(path: str) -> list:
    with open(path, "r") as file:
        jobs_reader = csv.DictReader(file)
        jobs = []
        for job in jobs_reader:
            jobs.append(job)
    return jobs
