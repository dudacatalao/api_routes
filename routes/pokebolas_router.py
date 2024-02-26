from fastapi import APIRouter

router = APIRouter()

@router.get('api/v1/pokemons')
async def get_pokebolas():
  return {'Mensagem' : 'Retornando tods as pokebolas'}
