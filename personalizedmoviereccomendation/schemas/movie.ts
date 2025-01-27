export default {
    name: "movie", // Unique name for the schema
    title: "Movie", // Display title in Studio
    type: "document", // This makes it a document type
    fields: [
      {
        name: "title",
        title: "Title",
        type: "string", // The type of field
      },
      {
        name: "releaseYear",
        title: "Release Year",
        type: "number",
      },
      {
        name: "genre",
        title: "Genre",
        type: "array", // Array of genres
        of: [{ type: "string" }],
      },
      {
        name: "description",
        title: "Description",
        type: "text",
      },
      {
        name: "tags",
        title: "Tags",
        type: "array", // Array of tags for recommendation
        of: [{ type: "string" }],
      },
      {
        name: "poster",
        title: "Poster",
        type: "image", // Image upload support
        options: {
          hotspot: true, // Enable image cropping
        },
      },
    ],
  };
  