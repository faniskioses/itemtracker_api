# use official python image
FROM python:3.11

# set working directory
WORKDIR /app

# copy requirements
COPY requirements.txt .

#install dependencies
RUN pip install --no-cache-dir -r requirements.txt

#copy the rest of the code
COPY . .

#run the fastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]