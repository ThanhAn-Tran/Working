# Pet Store - Full Stack Application

A complete Pet Store management system with FastAPI backend and frontend interface.

## Quick Setup Guide

### Prerequisites
- Python 3.8+
- PostgreSQL
- VS Code with Live Server extension

### Required VS Code Extensions
- **SQLTools** - Database management
- **SQLTools PostgreSQL/Cockroach Driver** - PostgreSQL connection
- **Live Server** - Frontend development server

## Backend Setup

1. **Extract and navigate to backend folder**
   ```bash
   cd working
   ```

2. **Activate virtual environment**
   ```bash
   # Windows
   petstore_env\Scripts\activate
   
   # macOS/Linux  
   source petstore_env/bin/activate
   ```

3. **Install dependencies** (if needed)
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup PostgreSQL Database**
   - Create database named `PetInfor`
   - Import database schema:
     ```bash
     psql -U <username> -d PetInfor -f mydb.sql
     ```

5. **Configure database connection**
   - Update database credentials in `app/database.py` if needed
   - Default: `postgresql://<username>:<password>@<host>/<database_name>`
   - Expected default: `postgresql://postgres:admin123@localhost/PetInfor`
   
6. **Run backend server**
   ```bash
   uvicorn app.main:app --reload
   ```
   
   Backend will run on: http://127.0.0.1:8000

## Frontend Setup

1. **Extract frontend folder**

2. **Open frontend folder in VS Code**

3. **Start Live Server**
   - Right-click on `index.html`
   - Select "Open with Live Server"
   - Ensure it runs on port **5500**: http://127.0.0.1:5500

## Running the Application

1. **Start backend first**: `uvicorn app.main:app --reload`
2. **Start frontend**: Use Live Server on port 5500
3. **Access application**: http://127.0.0.1:5500

## API Documentation
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Troubleshooting

### Database Issues
- Ensure PostgreSQL is running
- Check database name: `PetInfor`
- Import `mydb.sql` if tables don't exist

### CORS Issues
- Frontend must run on port 5500
- Backend configured for: http://127.0.0.1:5500

### Import Errors
- Activate virtual environment: `petstore_env\Scripts\activate`
- Install dependencies: `pip install -r requirements.txt`

## Project Structure
```
backend/
├── petstore_env/          # Virtual environment
├── app/
│   ├── main.py           # FastAPI application
│   ├── database.py       # Database configuration
│   ├── models.py         # Database models
│   ├── crud.py           # Database operations
│   ├── routers/pets.py   # API endpoints
│   └── schemas/pet.py    # Data validation
├── mydb.sql              # Database schema
└── requirements.txt      # Python dependencies

frontend/
├── index.html            # Main page
├── styles.css            # Styling
└── api.js               # API communication
```
