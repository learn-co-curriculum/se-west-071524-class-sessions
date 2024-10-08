import { createSlice } from '@reduxjs/toolkit'
import { pets } from '../../data/pets'

const petsSlice = createSlice({
    name: 'pets',
    initialState: pets,
    reducers: {
        adoptPet(state, action){
            return state.map(p => p.id == action.payload ? {...p, isAdopted: true} : p)
        }
    }
})

export const { adoptPet } = petsSlice.actions
export default petsSlice.reducer