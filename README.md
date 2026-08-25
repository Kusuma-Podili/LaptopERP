# LaptopERP - Enterprise Laptop Lifecycle & Hardware ERP

LaptopERP is a scalable, modular Enterprise Resource Planning system tailored for computer hardware manufacturers, distributors, refurbishing facilities, and enterprise IT asset managers.

## Key Highlights
- **50,000+ Lines of Code** of production-grade Python, Django, REST APIs, HTML/CSS/JS, automated tests, and documentation.
- **Granular Git History**: Commit log tracking architecture, domain modules, tests, and deployment setup.
- **7 Automated Test Suites**: Comprehensive test coverage across RBAC, inventory serials, procurement, workshop repairs, sales, tax engine, warranty RMA, and REST APIs.

## Quick Start
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run database migrations
python manage.py makemigrations
python manage.py migrate

# 3. Seed demo data
python manage.py seed_erp

# 4. Run test suites
python manage.py test

# 5. Start development server
python manage.py runserver
```
