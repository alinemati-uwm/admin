# ElevateDB Setup Instructions


docker run --name pgdev -e POSTGRES_DB=elevate_db -e POSTGRES_USER=eval_user -e POSTGRES_PASSWORD=eval_password -p 5432:5432 -d postgres