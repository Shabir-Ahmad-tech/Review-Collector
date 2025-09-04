"""
Smart Review Collector - Simplified Version
A Python tool for businesses to collect and manage customer reviews
Used AI to make it user-friendly and efficient
"""

import json
import csv
import random
from datetime import datetime
from collections import defaultdict

class ReviewCollector:
    def __init__(self):
        self.customers = []
        self.reviews = []
        self.load_data()
    
    def load_data(self):
        """Load existing data from files if available"""
        try:
            with open('customers.json', 'r') as f:
                self.customers = json.load(f)
        except FileNotFoundError:
            self.customers = []
            
        try:
            with open('reviews.json', 'r') as f:
                self.reviews = json.load(f)
        except FileNotFoundError:
            self.reviews = []
    
    def save_data(self):
        """Save data to JSON files"""
        with open('customers.json', 'w') as f:
            json.dump(self.customers, f, indent=4)
            
        with open('reviews.json', 'w') as f:
            json.dump(self.reviews, f, indent=4)
    
    def add_customer(self, name, email, product):
        """Add a new customer to the system"""
        customer_id = len(self.customers) + 1
        customer = {
            'id': customer_id,
            'name': name,
            'email': email,
            'product': product,
            'join_date': datetime.now().strftime("%Y-%m-%d")
        }
        self.customers.append(customer)
        self.save_data()
        return customer_id
    
    def add_review(self, customer_id, rating, comment):
        """Add a review from a customer"""
        # Find customer
        customer = next((c for c in self.customers if c['id'] == customer_id), None)
        if not customer:
            return False
            
        review_id = len(self.reviews) + 1
        review = {
            'id': review_id,
            'customer_id': customer_id,
            'customer_name': customer['name'],
            'product': customer['product'],
            'rating': rating,
            'comment': comment,
            'date': datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        self.reviews.append(review)
        self.save_data()
        return True
    
    def generate_report(self):
        """Generate a luxury-styled report of reviews"""
        if not self.reviews:
            return "No reviews available yet."
        
        # Calculate stats
        total_reviews = len(self.reviews)
        avg_rating = sum(r['rating'] for r in self.reviews) / total_reviews
        products = defaultdict(list)
        for review in self.reviews:
            products[review['product']].append(review['rating'])
        
        # Create report with luxury styling
        report = []
        report.append("╔══════════════════════════════════════════════════╗")
        report.append("║               LUXURY REVIEW REPORT               ║")
        report.append("╠══════════════════════════════════════════════════╣")
        report.append(f"║  Total Reviews: {total_reviews:36} ║")
        report.append(f"║  Average Rating: {avg_rating:.1f}/5 {'⭐' * int(avg_rating):27} ║")
        report.append("╠══════════════════════════════════════════════════╣")
        
        # Add product breakdown
        for product, ratings in products.items():
            avg = sum(ratings) / len(ratings)
            report.append(f"║  {product:<25} {avg:.1f}/5 {'⭐' * int(avg):15} ║")
        
        report.append("╠══════════════════════════════════════════════════╣")
        report.append("║                 RECENT REVIEWS                  ║")
        report.append("╠══════════════════════════════════════════════════╣")
        
        # Add recent reviews (last 3)
        for review in self.reviews[-3:]:
            report.append(f"║  {review['date']:16} {review['rating']}/5 {review['customer_name']:20} ║")
            # Truncate long comments
            comment = review['comment'][:35] + "..." if len(review['comment']) > 35 else review['comment']
            report.append(f"║    \"{comment:<40}\" ║")
            report.append("║                                                ║")
        
        report.append("╚══════════════════════════════════════════════════╝")
        
        return "\n".join(report)
    
    def export_to_csv(self, filename="reviews_export.csv"):
        """Export reviews to a CSV file"""
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['id', 'customer_name', 'product', 'rating', 'comment', 'date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for review in self.reviews:
                writer.writerow({
                    'id': review['id'],
                    'customer_name': review['customer_name'],
                    'product': review['product'],
                    'rating': review['rating'],
                    'comment': review['comment'],
                    'date': review['date']
                })
        
        return f"Data exported to {filename}"

def display_luxury_menu():
    """Display a luxury-styled menu"""
    print("\n" + "═" * 50)
    print("            💎 SMART REVIEW COLLECTOR 💎")
    print("═" * 50)
    print("1. Add Customer")
    print("2. Add Review")
    print("3. Generate Report")
    print("4. Export to CSV")
    print("5. View All Data")
    print("6. Add Sample Data")
    print("7. Exit")
    print("═" * 50)

def main():
    collector = ReviewCollector()
    
    while True:
        display_luxury_menu()
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == "1":
            print("\n" + "─" * 30)
            print("ADD NEW CUSTOMER")
            print("─" * 30)
            name = input("Customer Name: ")
            email = input("Customer Email: ")
            product = input("Product Purchased: ")
            customer_id = collector.add_customer(name, email, product)
            print(f"✅ Customer added successfully! ID: {customer_id}")
            
        elif choice == "2":
            print("\n" + "─" * 30)
            print("ADD NEW REVIEW")
            print("─" * 30)
            try:
                customer_id = int(input("Customer ID: "))
                rating = int(input("Rating (1-5): "))
                if rating < 1 or rating > 5:
                    print("❌ Rating must be between 1 and 5")
                    continue
                comment = input("Review Comment: ")
                if collector.add_review(customer_id, rating, comment):
                    print("✅ Review added successfully!")
                else:
                    print("❌ Customer ID not found!")
            except ValueError:
                print("❌ Please enter valid numbers for ID and rating")
                
        elif choice == "3":
            print("\n" + "─" * 30)
            print("REVIEW REPORT")
            print("─" * 30)
            print(collector.generate_report())
            
        elif choice == "4":
            filename = input("Export filename (default: reviews_export.csv): ").strip()
            if not filename:
                filename = "reviews_export.csv"
            result = collector.export_to_csv(filename)
            print(f"✅ {result}")
            
        elif choice == "5":
            print("\n" + "─" * 30)
            print("ALL DATA")
            print("─" * 30)
            print("CUSTOMERS:")
            for customer in collector.customers:
                print(f"  {customer['id']}: {customer['name']} ({customer['email']}) - {customer['product']}")
            
            print("\nREVIEWS:")
            for review in collector.reviews:
                print(f"  {review['id']}: {review['customer_name']} - {review['rating']}/5 - {review['comment'][:30]}...")
                
        elif choice == "6":
            # Add some sample data
            sample_customers = [
                ("Emma Johnson", "emma@example.com", "Premium Watch"),
                ("James Smith", "james@example.com", "Designer Handbag"),
                ("Sophia Williams", "sophia@example.com", "Luxury Perfume"),
                ("Michael Brown", "michael@example.com", "Silk Scarf"),
                ("Olivia Davis", "olivia@example.com", "Leather Wallet")
            ]
            
            sample_reviews = [
                (1, 5, "Exceptional quality and craftsmanship. Absolutely love it!"),
                (1, 4, "Beautiful product, though delivery took a bit long."),
                (2, 5, "This is exactly what I was looking for. Perfect gift!"),
                (3, 3, "Nice product but the scent doesn't last as long as I hoped."),
                (4, 5, "The material is so luxurious. Definitely worth the price."),
                (5, 4, "Great quality and the packaging was exquisite.")
            ]
            
            for customer in sample_customers:
                collector.add_customer(*customer)
                
            for review in sample_reviews:
                collector.add_review(*review)
                
            print("✅ Sample data added successfully!")
            
        elif choice == "7":
            print("💎 Thank you for using Smart Review Collector!")
            break
            
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()