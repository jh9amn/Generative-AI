# 🚀 Neo4j Cypher Guide

> ```https://console.neo4j.io/projects/cd23b7e6-51e9-4a60-8e33-fbe0cb4385f1/tools/query```


This guide explains your entire query step-by-step from scratch in a **simple and structured way**.

---

# 📌 1. What is Neo4j?

Neo4j is a **graph database** where:

* Data is stored as **Nodes (entities)**
* Connections are **Relationships**
* Both can have **properties (key-value pairs)**

---

# 📌 2. Basic Concepts

## 🔹 Node

```
CREATE (n)
```

* Creates a simple node without label or properties

## 🔹 Node with Label

```
CREATE (Elon:CEO)
```

* Creates node with label `CEO`

## 🔹 Multiple Labels

```
CREATE (Elon:CEO:employee)
```

* Node has multiple labels: `CEO` and `employee`

---

# 📌 3. Fetching Data

## Get all employees

```
MATCH (n:employee) RETURN n LIMIT 25;
```

## Get all relationships

```
MATCH p=()-[]->() RETURN p LIMIT 25;
```

---

# 📌 4. Adding Properties

```
CREATE (Elon:CEO {
  name: "Elon Musk",
  YOB: 1979,
  POB: "SA"
})
```

* `name` → Name
* `YOB` → Year of Birth
* `POB` → Place of Birth

---

# 📌 5. Query Specific Properties

## Get all names

```
MATCH (n)
WHERE n.name IS NOT NULL
RETURN DISTINCT n.name
```

## Get all places of birth

```
MATCH (n)
WHERE n.POB IS NOT NULL
RETURN DISTINCT n.POB
```

---

# 📌 6. Creating Relationships

## Example: Elon is CEO of Tesla

```
CREATE (Tesla:Company {name:"Tesla"})
CREATE (Elon)-[:CEO]->(Tesla)
```

## Query relationship

```
MATCH p=()-[:CEO]->() RETURN p;
```

---

# 📌 7. More Node Examples

```
CREATE (Aman:enterpreneur {
  name:"Aman",
  YOB:2002,
  POB:"India"
})

CREATE (Ind:Country {name:"India"})
```

---

# 📌 8. Movie Example (Classic Neo4j Demo)

## Create nodes

```
CREATE (p:Person {name:"Tom Hanks", born:1956})
CREATE (m:Movie {title:"Forest Gump", released:1994})
```

## Create relationship

```
CREATE (p)-[:ACTED_IN]->(m)
```

## Query

```
MATCH (p:Person)-[:ACTED_IN]->(m:Movie)
RETURN p, m
```

---

# 📌 9. Update Data

```
MATCH (p:Person {name:"Tom Hanks"})
SET p.born = 1957
RETURN p
```

---

# 📌 10. Load Data from CSV

## Load Users

```
LOAD CSV WITH HEADERS FROM "URL" AS row
CREATE (:User {
  userId: toInteger(row.userId),
  name: row.name,
  age: toInteger(row.age),
  city: row.city
});
```

## Load Posts

```
LOAD CSV WITH HEADERS FROM "URL" AS row
MATCH (u:User {userId: toInteger(row.userId)})
CREATE (u)-[:POSTED]->(:Post {
  postId: toInteger(row.postId),
  content: row.content,
  timestamp: datetime(row.timestamp)
});
```

## Load Relationships

```
LOAD CSV WITH HEADERS FROM "URL" AS row
MATCH (u1:User {userId: toInteger(row.userId1)}),
      (u2:User {userId: toInteger(row.userId2)})
CREATE (u1)-[:FRIEND]->(u2)
CREATE (u1)-[:LIKES]->(u2);
```

---

# 📌 11. Querying Graph Data

## Get friends of John

```
MATCH (u:User {name:"John"})-[:FRIEND]-(f:User)
RETURN f.name;
```

## Get friends' posts

```
MATCH (u:User {name:"John"})-[:FRIEND]-(f:User)
      -[:POSTED]->(p:Post)
RETURN f.name, p.content;
```

## Who liked John's posts

```
MATCH (u:User {name:"John"})-[:POSTED]->(p:Post)
      <-[:LIKES]-(l:User)
RETURN l.name, p.content;
```

---

# 📌 12. Important Concepts Summary

| Concept  | Meaning                    |
| -------- | -------------------------- |
| CREATE   | Create nodes/relationships |
| MATCH    | Query data                 |
| WHERE    | Filter data                |
| RETURN   | Output result              |
| SET      | Update properties          |
| LOAD CSV | Import data                |

---

# 🎯 Final Understanding

You built:

* Basic nodes (CEO, Person, Company)
* Relationships (CEO, ACTED_IN, FRIEND, LIKES)
* Real dataset using CSV
* Complex queries (friends, posts, likes)

---

# 🚀 Next Steps (Recommended)

* Learn **MERGE vs CREATE**
* Learn **indexes & constraints**
* Practice **graph queries (depth traversal)**
* Build a **real project (social network or recommendation system)**


