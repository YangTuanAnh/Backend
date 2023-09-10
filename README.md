### Instruction

0. Put the private files into folder foodfeed_app (.env and .json files)

1. Update the conda

```
conda update --all
```

3. Create a new virtual environment with Python and activate it.

```
cd Backend/
python -m venv env
source env/bin/activate
```

**Suggestion**: Using `conda`  if you don't want to use Python venv.
```
conda create -n backend
conda activate backend
```

2. Install the dependencies (The hardest one)

```
conda install -r requirements.txt
```

- if the installation fails, run the below code to check missing modules.

  ```
  python manage.py runserver
  ```

  Some modules may occur for installation.

  ```
  pip install supabase
  pip install psycopg2
  pip install django-cors-headers
  ```

3. Run the application (make sure you have PostgreSQL running on your machine and please change the database settings in settings.py to your own database settings...)

    ```
    python manage.py makemigrations
    python manage.py migrate 
    python manage.py runserver
    ```
4. *(Optional - Should use when running on a server)* Deploy Backend on **ngrok**

- Open a new terminal and run **ngrok**:
    ```
    ngrok http 8000
    ```

- If not using **ngrok**, just use the localhost [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
