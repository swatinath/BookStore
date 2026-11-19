
# 📚 BookStore — End-to-End D2C E-Commerce & Inventory Management Platform

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-Framework-092E20?style=for-the-badge&logo=django&logoColor=white)
![SQL](https://img.shields.io/badge/Database-Relational_SQL-4479A1?style=for-the-badge&logo=postgresql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Production_Ready-success?style=for-the-badge)

> **Bridging Independent Retail Operations with Modern Digital Commerce.**  
> A full-stack, single-vendor D2C e-commerce platform built with Django to digitize catalog management, streamline order fulfillment, and enhance customer retention for independent bookstores.

---

## 🎯 Business Context & Value Proposition

Independent brick-and-mortar bookstores often struggle to compete with major e-commerce aggregators due to high marketplace commissions (15%–30% per order) and lack of customer data ownership. **BookStore** solves this by providing a proprietary, direct-to-consumer (D2C) storefront tailored for a single retail entity.

### Key Business Outcomes
* **Margin Protection:** Eliminates third-party aggregator fees by enabling direct customer acquisition and order fulfillment.
* **Inventory & Catalog Agility:** Empowers store operators to dynamically update stock availability (`is_available`), pricing, and genre categorization in real time.
* **Trust & Conversion Optimization:** Integrates verified customer ratings and moderated reviews (`is_visible`) to drive social proof and reduce purchase friction.
* **Frictionless Checkout Experience:** Supports multi-address management and persistent cart workflows to minimize cart abandonment.

---

## 👥 User Personas & Functional Scope

The platform is architected around a **two-sided operational model**, separating storefront customer journeys from back-office retail operations.

### 1. Store Administrator (Seller / Operations)
*Designed for store owners and inventory managers to control catalog merchandising and order pipelines.*
* **Authentication & Security:** Role-based login, logout, and profile management.
* **Category Merchandising (CRUD):** Create, update, and organize book genres to optimize product discovery.
* **Catalog & Inventory Management (CRUD):** Add new titles, manage metadata (author, publisher, publication year), set pricing, upload cover assets, and toggle real-time stock status.
* **Order Fulfillment Pipeline (Read / Update):** Track incoming customer orders and update fulfillment statuses (e.g., *Pending → Shipped → Delivered*).

### 2. Customer (End-User / Buyer)
*Designed for seamless browsing, evaluation, and repeat purchasing.*
* **Product Discovery:** Browse the complete catalog, filter books by category, and inspect detailed product pages.
* **Account & Address Book (CRUD):** Self-service registration, authentication, profile updates, and multiple delivery address management.
* **Shopping Cart & Checkout (CRUD):** Dynamic cart state management with automated quantity and total price calculation.
* **Order Tracking & Lifecycle (CRUD):** Place orders, view order history, and manage active requests.
* **Social Proof & Engagement (Create / Read):** Submit ratings and written reviews on purchased titles to inform future buyers.

---

## 🏗️ System Architecture & Modular Design

Built on Django's **MVT (Model-View-Template)** architectural pattern, the codebase is decoupled into four domain-specific applications for maintainability and scalability:

```text
BookStore/
├── admin_panel/    # Back-office operations, inventory CRUD, and order status workflows
├── user/           # Authentication, role-based access control (RBAC), profiles, and address book
├── book/           # Core product engine: catalog, categories, cart logic, orders, and reviews
└── pages/          # Customer-facing storefront views (Home/Index, About, Contact)

```

---

## 🗄️ Database Schema & Entity Relationships

The relational data model enforces referential integrity across users, inventory, fulfillment, and user-generated content.

### Core Entities

| Table | Primary Key | Foreign Keys | Key Attributes & Business Logic |
| --- | --- | --- | --- |
| **`User`** | `id` | — | Leverages Django's built-in `auth_user` model for secure credential hashing and role differentiation (Admin vs. Customer). |
| **`Category`** | `id` | — | `category` — Taxonomy grouping for catalog navigation and merchandising. |
| **`Book`** | `id` | `category_id` | `title`, `author`, `publisher`, `publication_year`, `description`, `price`, `image`, `is_available` (stock flag). |
| **`Address`** | `id` | `user_id` | `addressline_one`, `addressline_two`, `locality`, `landmark`, `city`, `state`, `zip` — Supports multiple shipping destinations per user. |
| **`Order`** | `id` | `user_id`, `book_id`, `address_id` | `quantity`, `total_price`, `status` — Captures transactional state and links inventory to fulfillment logistics. |
| **`Review`** | `id` | `user_id`, `book_id` | `rating`, `comment`, `created_at`, `is_visible` — Enables moderated customer feedback loops. |

### Entity-Relationship Overview
```
erDiagram
    USER ||--o{ ADDRESS : "saves"
    USER ||--o{ ORDER : "places"
    USER ||--o{ REVIEW : "writes"
    CATEGORY ||--o{ BOOK : "classifies"
    BOOK ||--o{ ORDER : "included in"
    BOOK ||--o{ REVIEW : "receives"
    ADDRESS ||--o{ ORDER : "ships to"
```
---

## 🚀 Getting Started (Local Setup)

### Prerequisites

* Python 3.8+
* pip & virtualenv

### Installation Steps

1. **Clone the repository**
```bash
git clone [https://github.com/yourusername/bookstore.git](https://github.com/yourusername/bookstore.git)
cd bookstore

```


2. **Create and activate a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```


3. **Install dependencies**
```bash
pip install -r requirements.txt

```


4. **Apply database migrations**
```bash
python manage.py makemigrations
python manage.py migrate

```


5. **Create an Admin superuser**
```bash
python manage.py createsuperuser

```


6. **Run the development server**
```bash
python manage.py runserver

```


Access the storefront at `http://127.0.0.1:8000/` and the admin portal at `http://127.0.0.1:8000/admin/`.

---

## 🔮 Future Product Roadmap

To evolve this MVP into an enterprise-grade retail platform, the next product iterations include:

* **Payment Gateway Integration:** Adding Razorpay/Stripe webhooks for automated payment reconciliation.
* **Normalized Order-Item Architecture:** Introducing an `OrderItem` junction table to support multi-book single-checkout transactions.
* **Recommendation Engine:** Collaborative filtering ("Customers who bought this also bought...") to increase Average Order Value (AOV).
* **Analytics Dashboard:** Admin KPI tracking for conversion rates, top-performing genres, and inventory turnover.
