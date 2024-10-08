import { configureStore } from '@reduxjs/toolkit'
import budgetReducer from '../features/budget/budgetSlice'
import petsReducer from '../features/pets/petsSlice'
import { petsApi } from "./services/petsApi"

export const store = configureStore({

    // configureStore is a
    // wrapper around createStore but sets it up with defaults
    // sets up redux-dev-tools
    // adds Thunk middleware
    // uses combineReducers as necessary

    reducer: {
        budget: budgetReducer,
        // pets: petsReducer,
        [petsApi.reducerPath]: petsApi.reducer
    },
    middleware: (getDefaultMiddleware) => {
        return getDefaultMiddleware().concat(petsApi.middleware)
    }

})