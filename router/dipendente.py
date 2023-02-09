import email
from fastapi import APIRouter, status , HTTPException   

from dao.dipendente_dao import Dipendente_dao

from models.dipendente import Dipendente_model

from typing import List

router = APIRouter(prefix='/dipendente', tags=['dipendente'])


@router.get(
    '/all',
    response_model=List[Dipendente_model],
    response_model_exclude_none=True,
    response_model_include={'id_dipendente', 'nome', 'cognome', 'cf', 'iban', 'id_tipo_contratto', 'email', 'telefono', 'data_nascita'})
async def get_dipendente():
    return Dipendente_dao.get_all_employees()

@router.get(
    '/employee',
    response_model=List[Dipendente_model],
    response_model_exclude_none=True,
    response_model_include={'id_dipendente', 'nome', 'cognome', 'cf', 'iban', 'id_tipo_contratto', 'email', 'telefono', 'data_nascita'})
    
async def get_dipendente(id: str):
    return Dipendente_dao.get_employee_by_id(id)


# @router.get("")
# async def prendi_dipendente(id_dipendente: str):
#     if Dipendente_dao.get_all_employees() == [] :
#         raise HTTPException (status_code=404, detail="Nessun dipendente trovata")
#     try:  
#         return Dipendente_dao.get_all_employees()
#     except Exception as e:
#         raise HTTPException (status_code=500, detail=e.msg)
        
@router.post('/new')
async def addEmployee(employee :Dipendente_model):
  return Dipendente_dao.insert_employee(employee.id_dipendente, employee.nome, employee.cognome, employee.cf,
                                        employee.iban, employee.id_tipo_contratto, employee.email, employee.telefono, employee.data_nascita)

@router.put('/update')
async def updateCompany(employee: Dipendente_model):
    return Dipendente_dao.update_employee(employee.id_dipendente, employee.nome, employee.cognome, employee.cf,
                                        employee.iban, employee.id_tipo_contratto, employee.email, employee.telefono, employee.data_nascita)

@router.delete('/delete')
async def deleteCompany(dipendente: str):
    return Dipendente_dao.delete_employee(dipendente)
