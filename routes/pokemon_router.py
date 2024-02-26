from fastapi import APIRouter

router = APIRouter()

@router.get('api/v1/pokemons')
async def get_pokemon():
  return {'Mensagem' : 'Retornando tods as pokemon'}
