---
tags: ["backend", "java", "kubernetes-native"]
---
# Framework: Quarkus

## Schema: Framework Specification

- framework: Quarkus
- category: backend
- language: Java
- latest_supported_version: 3.x
- rendering_engine: N/A
- state_management: Panache ORM
- router: RESTEasy
- build_tool: Maven/Gradle

---

## Core Stack

- **Build**: Maven / Gradle.
- **Paradigm**: Reactive.

## Golden Snippet

```java
import jakarta.ws.rs.GET;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.Produces;
import jakarta.ws.rs.core.MediaType;

@Path("/hello")
public class GreetingResource {

    @GET
    @Produces(MediaType.TEXT_PLAIN)
    public String hello() {
        return "Hello from Quarkus REST";
    }
}
```
