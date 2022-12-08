import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("key.json")
obj = firebase_admin.initialize_app(cred, { 'databaseURL': "https://loggbwv-default-rtdb.firebaseio.com/"})

def update():

    ref1 = db.reference('/House1')
    ref2 = db.reference('/House2')

    h1Volume = input("H1 Volule :")
    h1Weight = input("H1 Weight :")

    h2Volume = input("H2 Volume :")
    h2Weight = input("H2 Weight :")
    ref1.set(
        {
            'GarbageVolume': h1Volume,
            'GarbageWeight': h1Weight
        }
    )

    ref2.set(
        {
            'GarbageVolume': h2Volume,
            'GarbageWeight': h2Weight
        }
    )

for x in range(1,10):
    print(f'Iteration : {x}')
    update()
  
else:
    print("Finished 10 iterations")
    