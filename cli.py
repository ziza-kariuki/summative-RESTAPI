import requests

base_url = "http://127.0.0.1:5000"

def show_menu():
    print("\n==================================")
    print("   INVENTORY MANAGEMENT SYSTEM    ")
    print("==================================")
    print("1. View all inventory items")
    print("2. Search OpenFoodFacts API")
    print("3. Add new inventory item")
    print("4. Update item details")
    print("5. Delete an item")
    print("6. Exit")

def run_cli():
    while True:
        show_menu()
        choice = input("\nSelect an option (1-6): ").strip()

        try:
            # 1. View Inventory
            if choice == "1":
                response = requests.get(f"{base_url}/inventory")
                if response.status_code == 200:
                    items = response.json()
                    print("\n--- Current Inventory ---")
                    for item in items:
                        print(f"ID: {item.get('status')} | Product: {item.get('product', {}).get('product_name') or item.get('product', {}).get('product_name_en')}")
                else:
                    print("\nError: Unable to retrieve inventory.")

            # 2. Search External API
            elif choice == "2":
                query = input("Enter barcode or product name: ").strip()
                if not query:
                    print("Search query cannot be empty.")
                    continue
                
                response = requests.get(f"{base_url}/external/{query}")
                if response.status_code == 200:
                    print("\n--- External API Result ---")
                    print(response.json())
                else:
                    print("\nProduct not found on OpenFoodFacts.")

            # 3. Add Item
            elif choice == "3":
                try:
                    item_id = int(input("Enter new item ID number: "))
                    name = input("Enter product name: ").strip()
                    brand = input("Enter brand name: ").strip()
                    
                    template = {
                        "status": item_id,
                        "product": {
                            "product_name": name,
                            "brands": brand
                        }
                    }
                    response = requests.post(f"{base_url}/inventory", json=template)
                    print(f"\nResponse: {response.json().get('message')}")
                except ValueError:
                    print("Invalid input! Item ID must be a number.")

            # 4. Update Item(Renaming)
            elif choice == "4":
                try:
                    item_id = int(input("Enter item ID to update: "))
                    new_name = input("Enter new product name: ").strip()
                    
                    template = {"product": {"product_name": new_name}}
                    response = requests.patch(f"{base_url}/inventory/{item_id}", json=template)
                    
                    if response.status_code == 200:
                        print("\nItem updated successfully!")
                    else:
                        print("\nItem not found.")
                except ValueError:
                    print("Invalid input! Item ID must be a number.")

            # 5. Delete Item
            elif choice == "5":
                try:
                    item_id = int(input("Enter item ID to delete: "))
                    response = requests.delete(f"{base_url}/inventory/{item_id}")
                    if response.status_code == 200:
                        print(f"\nItem {item_id} deleted successfully.")
                    else:
                        print("\nItem not found.")
                except ValueError:
                    print("Invalid input! Item ID must be a number.")

            # 6. Exit
            elif choice == "6":
                print("\nExiting App. Goodbye!")
                break
            else:
                print("Invalid option. Please choose between 1 and 6.")

        except requests.exceptions.ConnectionError:
            print("\nConnection Error: Make sure your Flask server is running on port 5000!")

if __name__ == "__main__":
    run_cli()