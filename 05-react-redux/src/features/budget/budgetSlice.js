import { createSlice } from "@reduxjs/toolkit"

const initialState = { value: 100 }

const budgetSlice = createSlice({
    name: 'budget',
    initialState,
    // immer lib lets us write state change as a mutation, but clones state and replaces with new state
    reducers: {
        addTen(state) {
            state.value += 10
        },
        subtractAmount(state, action) {
            state.value -= action.payload
        }
    }

})

export const { addTen, subtractAmount } = budgetSlice.actions
export default budgetSlice.reducer