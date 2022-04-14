import requests

def get_pokemon_info(poke_id):

      print("Getting Pokemon Information...", end= " ")
      poke_id = poke_id.strip().lower()
      if poke_id in (None, ''):
        return
      response = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(poke_id))

      if response.status_code == 200:
        print('Success')
        return response.json()
      else:
        print('Failed, Response code:', response.status_code)
        return