# Purchase-Workflow
Practicing Django's ORM and recreating a purchase workflow I've developed in my day-to-day

If you'd like to run this locally then please do!
Just make sure to activate the virtual environment before running the server. 
```
source pwvenv/bin/activate
```
```
cd purchase_workflow
```
```
python3 manage.py runserver
```

6-23-23:
- Completely forgot to push the initial commit, so here we are with a giant first commit
- Created the PurchaseOrder, Vendor, and Product models
- Began trying to modify the built in Django **User** model to include more fields
- Added Create buttons (currently only works on **Vendors** and **Products**)
- Kanban <-> List view swapping
- List/Kanban Views opening an editable **Form** view (it's literally the form)
- A lot of mundane things in HTML and CSS like making the Kanban cards _grow_ when you hover them, to struggling to format the Form views to fit on a card
