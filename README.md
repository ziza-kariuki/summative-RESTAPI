# Python REST API with Flask- Product Management System 

A RESTful Flask API integrated with external data from the OpenFoodFacts API for managing product inventory. Can be interacted with through a CLI-based interface.

## Features
* **Product Registration**: Create new product profiles
* **Data Storage**: All product info is stored locally for future reference
* **Data Retrieval**: App is connected to OpenFoodFcats api to get specific data from their database
* **User Interface**: Users can interact with routes through a command-line interface
* **Automated Testing**:Local tests are available to verify the functionality of the code with further updates


## How to run the project
## A. Initialize Virtual Environment & Dependencies
1. Clone the repository:
```bash
git clone <https://github.com/ziza-kariuki/summative-RESTAPI/blob/main>
cd summative-RESTAPI
```
2. Set up and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```
3. Install dependencies:
```bash
pip install flask requests pytest
```
4. Run the Flask server:
```bash
python3 app.py
```

## B. Running CLI commands(examples)
1. Launch the CLI:
```bash
python3 cli.py
```
2. View inventory: Fetch and list all items currently in stock:
```text
Select an option (1-6): 1

--- Current Inventory ---
ID: 101 | Product: Organic Almond Milk
ID: 102 | Product: Rice Noodles

```

3. Search OpenFoodFacts:
```text
Select an option (1-6): 2
Enter barcode or product name: 737628064502

--- External API Result ---
{
  "status": 1,
  "product": {
    "product_name": "Organic Almond Milk",
    "brands": "Silk",
    "ingredients_text": "Filtered water, almonds..."
  }
}
``

4. Add item: 
```text
Select an option (1-6): 3
Enter new item ID/Status number: 103
Enter product name: Dark Chocolate Bar
Enter brand name: Lindt

Response: Item added successfully
```

5. Update item:
```text
Select an option (1-6): 4
Enter item ID to update: 103
Enter new product name: Lindt 85% Dark Chocolate

Item updated successfully!
```

6. Delete item:
```text
Select an option (1-6): 5
Enter item ID to delete: 103

Item 103 deleted successfully.
```

7. Exit: Close the CLI.
```text
Select an option (1-6): 6
```

## C. Running Automated tests
To execute the test suite, run from the root directory:
```bash
pytest
```

## API endpoint details
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/inventory` | Fetch all inventory items |
| `POST` | `/inventory` | Add a new inventory item |
| `PATCH` | `/inventory/<id>` | Update an existing item |
| `DELETE` | `/inventory/<id>` | Remove an item by ID|
| `GET` | `/external/<query>` | Query OpenFoodFacts API|

## Technologies Used
Language: Python 3.12
Internal Modules: unittest, flask, jsonify, requests
