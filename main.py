from fastapi import FastAPI
from controller.openai_controller import router as openai_router
from fastapi.responses import HTMLResponse

app = FastAPI()

app.include_router(openai_router, prefix="/openai", tags=["OpenAI"])


@app.get("/", response_class=HTMLResponse)
def read_root() -> HTMLResponse:
    """
    Root endpoint that returns a sample HTML page.

    Returns:
        HTMLResponse: An HTML response containing a sample HTML page.
    """
    html_content = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PL/SQL Error Codes and Solutions</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        h1 {
            color: #333;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        tr:hover {
            background-color: #f1f1f1;
        }
    </style>
</head>
<body>
    <h1>PL/SQL Error Codes and Solutions</h1>
    <p>PL/SQL (Procedural Language/Structured Query Language) is Oracle Corporation's procedural extension for SQL and the Oracle relational database. Below are some common PL/SQL error codes, their descriptions, and solutions:</p>
    
    <table>
        <thead>
            <tr>
                <th>Error Code</th>
                <th>Description</th>
                <th>Solution</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>ORA-00001</td>
                <td>Unique constraint violated.</td>
                <td>Ensure that the value being inserted is unique and does not violate any unique constraints on the table.</td>
            </tr>
            <tr>
                <td>ORA-00904</td>
                <td>Invalid column name.</td>
                <td>Check the column names in your SQL statement for typos or incorrect names. Verify that the column exists in the table.</td>
            </tr>
            <tr>
                <td>ORA-01400</td>
                <td>Cannot insert NULL into a column that does not allow NULLs.</td>
                <td>Ensure that you are providing a value for all columns that do not allow NULLs. Check the table definition for columns with NOT NULL constraints.</td>
            </tr>
            <tr>
                <td>ORA-01722</td>
                <td>Invalid number.</td>
                <td>Ensure that you are providing numeric values where required. Check for any non-numeric characters in fields that expect numbers.</td>
            </tr>
        </tbody>
    </table>
</body>
</html>
    """
    return HTMLResponse(content=html_content)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)