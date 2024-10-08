import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const petsApi = createApi({
  reducerPath: "petsApi",
  baseQuery: fetchBaseQuery({
    baseUrl: "/api",
  }),
  tagType: ["Pet"],
  endpoints(builder) {
    return {
    //   fetchPets: builder.query({
    //     query() {
    //       return "/pets";
    //     },
      fetchPets: builder.query({
        query(type) {
          return `/pets?type_like=${type}`;
        },
        // providesTags: ['Pet'] // Step 1: means total result of this query will be invalidated an re-fetched
        // If any mutation is executed that `invalidate`s any of these tags, this query will re-run to be always up-to-date.
        providesTags: (
            result,
            error,
            arg // Step 2: add ids to individual items to add granularity
          ) =>
            result
              ? [...result.map(({ id }) => ({ type: "Pet", id })), "Pet"]
              : ["Pet"], // Provides a list of `Pets` by `id`.
          // The `LIST` id is an arbitrary "virtual id" which would allow us to invalidate this query separately from those tagged more generally 'Pet'
          //     providesTags: (result) =>
          //     result // is result available?
          //     ? [...result.map(({id}) => ({id})), // successful query
          //     { id: 'LIST'},
          // ]
          // : [{id: 'LIST'}], // an error occurred, but we still want to refetch this query when `{ id: 'LIST' }` is invalidated
      }),
      updatePets: builder.mutation({
        query: ({ id, ...patch }) => ({
          url: `/pets/${id}`,
          method: "PATCH",
          body: patch,
        }),
         // invalidatesTags: ['Pet'], // Step 1: Invalidates all queries with the same tag
        // Step 2: invalidate by id
        // Invalidates all queries that subscribe to this Pet 'id' only.
        invalidatesTags: (results, error, arg) => [{ type: "Pet", id: arg.id }],
        // invalidatesTags: (results, error, { id }) => [{id}] // alt syntax
      }),
    };
  },
});

export const { useFetchPetsQuery, useUpdatePetsMutation } = petsApi;
