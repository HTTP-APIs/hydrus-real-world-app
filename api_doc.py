"""
Generated API Documentation for Server API using doc_generator.py."""

doc = {
    "@context": {
        "ApiDocumentation": "hydra:ApiDocumentation",
        "description": "hydra:description",
        "domain": {
            "@id": "rdfs:domain",
            "@type": "@id"
        },
        "expects": {
            "@id": "hydra:expects",
            "@type": "@id"
        },
        "hydra": "http://www.w3.org/ns/hydra/core#",
        "label": "rdfs:label",
        "method": "hydra:method",
        "possibleStatus": "hydra:possibleStatus",
        "property": {
            "@id": "hydra:property",
            "@type": "@id"
        },
        "range": {
            "@id": "rdfs:range",
            "@type": "@id"
        },
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "readonly": "hydra:readonly",
        "required": "hydra:required",
        "returns": {
            "@id": "hydra:returns",
            "@type": "@id"
        },
        "statusCode": "hydra:statusCode",
        "statusCodes": "hydra:statusCodes",
        "subClassOf": {
            "@id": "rdfs:subClassOf",
            "@type": "@id"
        },
        "supportedClass": "hydra:supportedClass",
        "supportedOperation": "hydra:supportedOperation",
        "supportedProperty": "hydra:supportedProperty",
        "title": "hydra:title",
        "vocab": "http://localhost:8080/api/vocab#",
        "writeonly": "hydra:writeonly"
    },
    "@id": "http://localhost:8080/api/vocab",
    "@type": "ApiDocumentation",
    "description": "Hydra API Documentation for Real-World App, realworld.io",
    "possibleStatus": [],
    "supportedClass": [
        {
            "@id": "vocab:Article",
            "@type": "hydra:Class",
            "description": "An article on social media, posted and dispalyed by this example app",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/FindAction",
                    "expects": "null",
                    "method": "GET",
                    "possibleStatus": [
                        {
                            "description": "Article not found",
                            "statusCode": 404
                        },
                        {
                            "description": "Article returned",
                            "statusCode": 200
                        }
                    ],
                    "returns": "vocab:Article",
                    "title": "GetArticle"
                },
                {
                    "@type": "http://schema.org/UpdateAction",
                    "expects": "vocab:Article",
                    "method": "POST",
                    "possibleStatus": [
                        {
                            "description": "Article updated",
                            "statusCode": 200
                        }
                    ],
                    "returns": "null",
                    "title": "UpdateArticle"
                },
                {
                    "@type": "http://schema.org/DeleteAction",
                    "expects": "null",
                    "method": "DELETE",
                    "possibleStatus": [
                        {
                            "description": "Article deleted",
                            "statusCode": 200
                        }
                    ],
                    "returns": "null",
                    "title": "DeleteArticle"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "https://schema.org/articleBody",
                    "readonly": "false",
                    "required": "true",
                    "title": "body",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://tal.schema.talaka.by/slug",
                    "readonly": "false",
                    "required": "true",
                    "title": "slug",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "https://schema.org/headline",
                    "readonly": "false",
                    "required": "true",
                    "title": "title",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "https://schema.org/description",
                    "readonly": "false",
                    "required": "true",
                    "title": "description",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/author",
                    "readonly": "false",
                    "required": "true",
                    "title": "author",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "vocab:article/favorites",
                    "readonly": "false",
                    "required": "false",
                    "title": "favorites",
                    "writeonly": "false"
                },
{
                    "@type": "SupportedProperty",
                    "property": {
                        "@id": "vocab:article/comments",
                        "@type": "hydra:Link",
                        "label": "comments",
                        "description": "The comments associated with this article",
                        "domain": "vocab:Article",
                        "range": "http://www.w3.org/ns/hydra/core#Collection",
                        "supportedOperation": [
                            {
                                "@id": "_:article_comment_create",
                                "@type": "hydra:Operation",
                                "method": "PUT",
                                "label": "Creates a new Comment for a specific issue",
                                "description": "To create a new Comment you have to be authenticated.",
                                "expects": "vocab:Comment",
                                "returns": "vocab:Comment",
                                "statusCodes": [
                                    {
                                        "code": 404,
                                        "description": "If the Article wasn't found."
                                    }
                                ]
                            },
                            {
                                "@id": "_:article_comment_collection_retrieve",
                                "@type": "hydra:Operation",
                                "method": "GET",
                                "label": "Retrieves all Comment entities for a specific article",
                                "description": "null",
                                "expects": "null",
                                "returns": "http://www.w3.org/ns/hydra/core#Collection",
                                "statusCodes": []
                            }
                        ]
                    },
                    "readonly": "false",
                    "required": "false",
                    "title": "comments",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "vocab:article/tags",
                    "readonly": "false",
                    "required": "false",
                    "title": "tagList",
                    "writeonly": "false"
                }
            ],
            "title": "Article"
        },
        {
            "@id": "vocab:Tag",
            "@type": "hydra:Class",
            "description": "A tag for the article",
            "supportedOperation": [],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "https://schema.org/name",
                    "readonly": "false",
                    "required": "true",
                    "title": "tagName",
                    "writeonly": "false"
                }
            ],
            "title": "Tag"
        },
        {
            "@id": "vocab:Comment",
            "@type": "hydra:Class",
            "description": "A comment on an article on social media, posted and dispalyed by this example app",
            "supportedOperation": [],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "https://schema.org/articleBody",
                    "readonly": "false",
                    "required": "true",
                    "title": "body",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "vocab:UserProfile",
                    "readonly": "false",
                    "required": "true",
                    "title": "author",
                    "writeonly": "false"
                }
            ],
            "title": "Comment"
        },
        {
            "@id": "vocab:UserProfile",
            "@type": "hydra:Class",
            "description": "Profile of the user",
            "supportedOperation": [],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "vocab:user",
                    "readonly": "false",
                    "required": "true",
                    "title": "user",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "vocab:UserProfile/follows",
                    "readonly": "false",
                    "required": "true",
                    "title": "follows",
                    "writeonly": "false"
                }
            ],
            "title": "UserProfile"
        },
        {
            "@id": "vocab:User",
            "@type": "hydra:Class",
            "description": "User handling an account",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/FindAction",
                    "expects": "null",
                    "method": "GET",
                    "possibleStatus": [
                        {
                            "description": "User not found",
                            "statusCode": 404
                        },
                        {
                            "description": "User returned",
                            "statusCode": 200
                        }
                    ],
                    "returns": "vocab:User",
                    "title": "GetUser"
                },
                {
                    "@type": "http://schema.org/UpdateAction",
                    "expects": "vocab:User",
                    "method": "POST",
                    "possibleStatus": [
                        {
                            "description": "User updated",
                            "statusCode": 200
                        }
                    ],
                    "returns": "null",
                    "title": "UpdateUser"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "https://schema.org/name",
                    "readonly": "false",
                    "required": "true",
                    "title": "username",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "https://schema.org/email",
                    "readonly": "false",
                    "required": "true",
                    "title": "email",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "https://schema.org/accessCode",
                    "readonly": "false",
                    "required": "true",
                    "title": "password",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "https://schema.org/description",
                    "readonly": "false",
                    "required": "true",
                    "title": "bio",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "https://schema.org/image",
                    "readonly": "false",
                    "required": "true",
                    "title": "image",
                    "writeonly": "false"
                }
            ],
            "title": "User"
        },
        {
            "@id": "http://www.w3.org/ns/hydra/core#Resource",
            "@type": "hydra:Class",
            "description": "null",
            "supportedOperation": [],
            "supportedProperty": [],
            "title": "Resource"
        },
        {
            "@id": "http://www.w3.org/ns/hydra/core#Collection",
            "@type": "hydra:Class",
            "description": "null",
            "supportedOperation": [],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readonly": "false",
                    "required": "null",
                    "title": "members",
                    "writeonly": "false"
                }
            ],
            "title": "Collection"
        },
        {
            "@id": "vocab:CommentCollection",
            "@type": "hydra:Class",
            "description": "A collection of comment",
            "subClassOf": "http://www.w3.org/ns/hydra/core#Collection",
            "supportedOperation": [
                {
                    "@id": "_:comment_collection_retrieve",
                    "@type": "http://schema.org/FindAction",
                    "description": "Retrieves all Comment entities",
                    "expects": "null",
                    "method": "GET",
                    "returns": "vocab:CommentCollection",
                    "statusCodes": []
                },
                {
                    "@id": "_:comment_create",
                    "@type": "http://schema.org/AddAction",
                    "description": "Create new Comment entitity",
                    "expects": "vocab:Comment",
                    "method": "PUT",
                    "returns": "vocab:Comment",
                    "statusCodes": [
                        {
                            "description": "If the Comment entity was createdsuccessfully.",
                            "statusCode": 201
                        }
                    ]
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "description": "The comment",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readonly": "false",
                    "required": "false",
                    "title": "members",
                    "writeonly": "false"
                }
            ],
            "title": "CommentCollection"
        },
        {
            "@id": "vocab:TagCollection",
            "@type": "hydra:Class",
            "description": "A collection of tag",
            "subClassOf": "http://www.w3.org/ns/hydra/core#Collection",
            "supportedOperation": [
                {
                    "@id": "_:tag_collection_retrieve",
                    "@type": "http://schema.org/FindAction",
                    "description": "Retrieves all Tag entities",
                    "expects": "null",
                    "method": "GET",
                    "returns": "vocab:TagCollection",
                    "statusCodes": []
                },
                {
                    "@id": "_:tag_create",
                    "@type": "http://schema.org/AddAction",
                    "description": "Create new Tag entitity",
                    "expects": "vocab:Tag",
                    "method": "PUT",
                    "returns": "vocab:Tag",
                    "statusCodes": [
                        {
                            "description": "If the Tag entity was createdsuccessfully.",
                            "statusCode": 201
                        }
                    ]
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "description": "The tag",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readonly": "false",
                    "required": "false",
                    "title": "members",
                    "writeonly": "false"
                }
            ],
            "title": "TagCollection"
        },
        {
            "@id": "vocab:UserCollection",
            "@type": "hydra:Class",
            "description": "A collection of user",
            "subClassOf": "http://www.w3.org/ns/hydra/core#Collection",
            "supportedOperation": [
                {
                    "@id": "_:user_collection_retrieve",
                    "@type": "http://schema.org/FindAction",
                    "description": "Retrieves all User entities",
                    "expects": "null",
                    "method": "GET",
                    "returns": "vocab:UserCollection",
                    "statusCodes": []
                },
                {
                    "@id": "_:user_create",
                    "@type": "http://schema.org/AddAction",
                    "description": "Create new User entitity",
                    "expects": "vocab:User",
                    "method": "PUT",
                    "returns": "vocab:User",
                    "statusCodes": [
                        {
                            "description": "If the User entity was createdsuccessfully.",
                            "statusCode": 201
                        }
                    ]
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "description": "The user",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readonly": "false",
                    "required": "false",
                    "title": "members",
                    "writeonly": "false"
                }
            ],
            "title": "UserCollection"
        },
        {
            "@id": "vocab:ArticleCollection",
            "@type": "hydra:Class",
            "description": "A collection of article",
            "subClassOf": "http://www.w3.org/ns/hydra/core#Collection",
            "supportedOperation": [
                {
                    "@id": "_:article_collection_retrieve",
                    "@type": "http://schema.org/FindAction",
                    "description": "Retrieves all Article entities",
                    "expects": "null",
                    "method": "GET",
                    "returns": "vocab:ArticleCollection",
                    "statusCodes": []
                },
                {
                    "@id": "_:article_create",
                    "@type": "http://schema.org/AddAction",
                    "description": "Create new Article entitity",
                    "expects": "vocab:Article",
                    "method": "PUT",
                    "returns": "vocab:Article",
                    "statusCodes": [
                        {
                            "description": "If the Article entity was createdsuccessfully.",
                            "statusCode": 201
                        }
                    ]
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "description": "The article",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readonly": "false",
                    "required": "false",
                    "title": "members",
                    "writeonly": "false"
                }
            ],
            "title": "ArticleCollection"
        },
        {
            "@id": "vocab:EntryPoint",
            "@type": "hydra:Class",
            "description": "The main entry point or homepage of the API.",
            "supportedOperation": [
                {
                    "@id": "_:entry_point",
                    "@type": "http://schema.org/FindAction",
                    "description": "The APIs main entry point.",
                    "expects": "null",
                    "method": "GET",
                    "returns": "null",
                    "statusCodes": "vocab:EntryPoint"
                }
            ],
            "supportedProperty": [
                {
                    "hydra:description": "The Article Class",
                    "hydra:title": "article",
                    "property": {
                        "@id": "vocab:EntryPoint/Article",
                        "@type": "hydra:Link",
                        "description": "An article on social media, posted and dispalyed by this example app",
                        "domain": "vocab:EntryPoint",
                        "label": "Article",
                        "range": "vocab:Article",
                        "supportedOperation": [
                            {
                                "@id": "getarticle",
                                "@type": "http://schema.org/FindAction",
                                "description": "null",
                                "expects": "null",
                                "label": "GetArticle",
                                "method": "GET",
                                "returns": "vocab:Article",
                                "statusCodes": [
                                    {
                                        "description": "Article not found",
                                        "statusCode": 404
                                    },
                                    {
                                        "description": "Article returned",
                                        "statusCode": 200
                                    }
                                ]
                            },
                            {
                                "@id": "updatearticle",
                                "@type": "http://schema.org/UpdateAction",
                                "description": "null",
                                "expects": "vocab:Article",
                                "label": "UpdateArticle",
                                "method": "POST",
                                "returns": "null",
                                "statusCodes": [
                                    {
                                        "description": "Article updated",
                                        "statusCode": 200
                                    }
                                ]
                            },
                            {
                                "@id": "deletearticle",
                                "@type": "http://schema.org/DeleteAction",
                                "description": "null",
                                "expects": "null",
                                "label": "DeleteArticle",
                                "method": "DELETE",
                                "returns": "null",
                                "statusCodes": [
                                    {
                                        "description": "Article deleted",
                                        "statusCode": 200
                                    }
                                ]
                            }
                        ]
                    },
                    "readonly": "true",
                    "required": "null",
                    "writeonly": "false"
                },
                {
                    "hydra:description": "The Comment Class",
                    "hydra:title": "comment",
                    "property": {
                        "@id": "vocab:EntryPoint/Comment",
                        "@type": "hydra:Link",
                        "description": "A comment on an article on social media, posted and dispalyed by this example app",
                        "domain": "vocab:EntryPoint",
                        "label": "Comment",
                        "range": "vocab:Comment",
                        "supportedOperation": []
                    },
                    "readonly": "true",
                    "required": "null",
                    "writeonly": "false"
                },
                {
                    "hydra:description": "The UserProfile Class",
                    "hydra:title": "userprofile",
                    "property": {
                        "@id": "vocab:EntryPoint/UserProfile",
                        "@type": "hydra:Link",
                        "description": "Profile of the user",
                        "domain": "vocab:EntryPoint",
                        "label": "UserProfile",
                        "range": "vocab:UserProfile",
                        "supportedOperation": []
                    },
                    "readonly": "true",
                    "required": "null",
                    "writeonly": "false"
                },
                {
                    "hydra:description": "The User Class",
                    "hydra:title": "user",
                    "property": {
                        "@id": "vocab:EntryPoint/User",
                        "@type": "hydra:Link",
                        "description": "User handling an account",
                        "domain": "vocab:EntryPoint",
                        "label": "User",
                        "range": "vocab:User",
                        "supportedOperation": [
                            {
                                "@id": "getuser",
                                "@type": "http://schema.org/FindAction",
                                "description": "null",
                                "expects": "null",
                                "label": "GetUser",
                                "method": "GET",
                                "returns": "vocab:User",
                                "statusCodes": [
                                    {
                                        "description": "User not found",
                                        "statusCode": 404
                                    },
                                    {
                                        "description": "User returned",
                                        "statusCode": 200
                                    }
                                ]
                            },
                            {
                                "@id": "updateuser",
                                "@type": "http://schema.org/UpdateAction",
                                "description": "null",
                                "expects": "vocab:User",
                                "label": "UpdateUser",
                                "method": "POST",
                                "returns": "null",
                                "statusCodes": [
                                    {
                                        "description": "User updated",
                                        "statusCode": 200
                                    }
                                ]
                            }
                        ]
                    },
                    "readonly": "true",
                    "required": "null",
                    "writeonly": "false"
                },
                {
                    "hydra:description": "The CommentCollection collection",
                    "hydra:title": "commentcollection",
                    "property": {
                        "@id": "vocab:EntryPoint/comments",
                        "@type": "hydra:Link",
                        "description": "The CommentCollection collection",
                        "domain": "vocab:EntryPoint",
                        "label": "CommentCollection",
                        "range": "vocab:CommentCollection",
                        "supportedOperation": [
                            {
                                "@id": "_:comment_collection_retrieve",
                                "@type": "http://schema.org/FindAction",
                                "description": "Retrieves all Comment entities",
                                "expects": "null",
                                "method": "GET",
                                "returns": "vocab:CommentCollection",
                                "statusCodes": []
                            },
                            {
                                "@id": "_:comment_create",
                                "@type": "http://schema.org/AddAction",
                                "description": "Create new Comment entitity",
                                "expects": "vocab:Comment",
                                "method": "PUT",
                                "returns": "vocab:Comment",
                                "statusCodes": [
                                    {
                                        "description": "If the Comment entity was createdsuccessfully.",
                                        "statusCode": 201
                                    }
                                ]
                            }
                        ]
                    },
                    "readonly": "true",
                    "required": "null",
                    "writeonly": "false"
                },
                {
                    "hydra:description": "The TagCollection collection",
                    "hydra:title": "tagcollection",
                    "property": {
                        "@id": "vocab:EntryPoint/tags",
                        "@type": "hydra:Link",
                        "description": "The TagCollection collection",
                        "domain": "vocab:EntryPoint",
                        "label": "TagCollection",
                        "range": "vocab:TagCollection",
                        "supportedOperation": [
                            {
                                "@id": "_:tag_collection_retrieve",
                                "@type": "http://schema.org/FindAction",
                                "description": "Retrieves all Tag entities",
                                "expects": "null",
                                "method": "GET",
                                "returns": "vocab:TagCollection",
                                "statusCodes": []
                            },
                            {
                                "@id": "_:tag_create",
                                "@type": "http://schema.org/AddAction",
                                "description": "Create new Tag entitity",
                                "expects": "vocab:Tag",
                                "method": "PUT",
                                "returns": "vocab:Tag",
                                "statusCodes": [
                                    {
                                        "description": "If the Tag entity was createdsuccessfully.",
                                        "statusCode": 201
                                    }
                                ]
                            }
                        ]
                    },
                    "readonly": "true",
                    "required": "null",
                    "writeonly": "false"
                },
                {
                    "hydra:description": "The UserCollection collection",
                    "hydra:title": "usercollection",
                    "property": {
                        "@id": "vocab:EntryPoint/users",
                        "@type": "hydra:Link",
                        "description": "The UserCollection collection",
                        "domain": "vocab:EntryPoint",
                        "label": "UserCollection",
                        "range": "vocab:UserCollection",
                        "supportedOperation": [
                            {
                                "@id": "_:user_collection_retrieve",
                                "@type": "http://schema.org/FindAction",
                                "description": "Retrieves all User entities",
                                "expects": "null",
                                "method": "GET",
                                "returns": "vocab:UserCollection",
                                "statusCodes": []
                            },
                            {
                                "@id": "_:user_create",
                                "@type": "http://schema.org/AddAction",
                                "description": "Create new User entitity",
                                "expects": "vocab:User",
                                "method": "PUT",
                                "returns": "vocab:User",
                                "statusCodes": [
                                    {
                                        "description": "If the User entity was createdsuccessfully.",
                                        "statusCode": 201
                                    }
                                ]
                            }
                        ]
                    },
                    "readonly": "true",
                    "required": "null",
                    "writeonly": "false"
                },
                {
                    "hydra:description": "The ArticleCollection collection",
                    "hydra:title": "articlecollection",
                    "property": {
                        "@id": "vocab:EntryPoint/articles",
                        "@type": "hydra:Link",
                        "description": "The ArticleCollection collection",
                        "domain": "vocab:EntryPoint",
                        "label": "ArticleCollection",
                        "range": "vocab:ArticleCollection",
                        "supportedOperation": [
                            {
                                "@id": "_:article_collection_retrieve",
                                "@type": "http://schema.org/FindAction",
                                "description": "Retrieves all Article entities",
                                "expects": "null",
                                "method": "GET",
                                "returns": "vocab:ArticleCollection",
                                "statusCodes": []
                            },
                            {
                                "@id": "_:article_create",
                                "@type": "http://schema.org/AddAction",
                                "description": "Create new Article entitity",
                                "expects": "vocab:Article",
                                "method": "PUT",
                                "returns": "vocab:Article",
                                "statusCodes": [
                                    {
                                        "description": "If the Article entity was createdsuccessfully.",
                                        "statusCode": 201
                                    }
                                ]
                            }
                        ]
                    },
                    "readonly": "true",
                    "required": "false",
                    "writeonly": "false"
                }
            ],
            "title": "EntryPoint"
        }
    ],
    "title": "API Doc for Real-World App"
}
