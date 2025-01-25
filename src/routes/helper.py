fake_users_db = {
  "johndoe": {
    "display_name": "John Doe",
    "first_name": "John Doe",
    "last_name": "John Doe",
    "email": "johndoe@example.com",
    "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
    "disabled": False,
  }
}

fake_companies_db = [
  {'id':1 , 'name':'Julies', 'specialty':'Pastries'},
  {'id':2 , 'name':'DOMAIN', 'specialty':'Netcafe'},
  {'id':3 , 'name':'TNC', 'specialty':'Netcafe', 
    'branches':[{ 'address':'11 Pelaez St, Cebu City, 6000 Cebu', 'contactNo':'(032) 266 1810'}]
  },
  {'id':4 , 'name':'Grafik9', 'specialty':'Printing'},
]