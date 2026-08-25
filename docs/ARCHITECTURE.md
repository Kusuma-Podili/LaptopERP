# LaptopERP Enterprise Architecture Specification

## 1. System Overview
LaptopERP is a modular, multi-tier Enterprise Resource Planning (ERP) platform built on Django 5.x and Django REST Framework. The system tracks the complete hardware lifecycle of laptop computers, component inventories, repair workshops, supply chains, sales channels, and customer warranty RMA workflows.

## 2. Core Subsystems
1. **Identity & RBAC (`core`)**: Provides fine-grained role-based permissions, multi-branch support, and immutable audit trails.
2. **Hardware Master & Serial Ledger (`inventory`)**: Manages CPU, RAM, GPU, and display specifications, condition grading (A+, A, B, C, Scrap), and serial number lifecycles.
3. **Warehouse & Logistics (`warehouse`)**: Manages physical locations, aisles, racks, shelves, bins, and stock transfers.
4. **Procurement & IQC (`procurement`)**: Purchase orders, vendor evaluation, and inward quality control inspection.
5. **Workshop & Refurbishing (`repairs`)**: Diagnostic checklists, job cards, parts requisitions, and labor cost accounting.
6. **Sales & Finance (`sales`)**: CRM, quotes, sales orders, GST/VAT tax calculation, and invoicing.
7. **Warranty & RMA (`warranty`)**: Warranty validity engine, RMA claim lifecycle, and replacement allocation.
8. **Executive BI (`analytics`)**: KPI calculations, turnover rates, defect heatmaps, and financial metrics.
9. **REST API Gateway (`api`)**: Token-authenticated RESTful API endpoints.
