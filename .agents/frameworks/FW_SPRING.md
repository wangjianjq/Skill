---
tags: ["backend", "java", "enterprise"]
---
# Framework: Spring Boot

## Schema: Framework Specification

- framework: Spring Boot
- category: backend
- language: Java
- latest_supported_version: 3.2+
- rendering_engine: Thymeleaf (optional)
- state_management: Spring Data JPA
- router: Spring MVC
- build_tool: Maven/Gradle

---

## [Modern] (Boot 3.2+, JDK 21+)

- **Java**: JDK 21+ mandatory for Virtual Threads.
- **Concurreny**: Enable Virtual Threads (`spring.threads.virtual.enabled=true`).
- **HTTP Client**: Prefer `RestClient` over `RestTemplate`.

### Modern Snippet

```java
@RestController
public class NativeController {
    private final RestClient restClient;
    public NativeController(RestClient.Builder builder) {
        this.restClient = builder.build();
    }
}
```

## [Stable/Legacy] (Boot 2.7 - 3.1)

- **Java**: JDK 8 - 17.
- **Patterns**: Reactive (`WebFlux`) for high concurrency (pre-virtual threads).
- **HTTP Client**: `RestTemplate` or `WebClient`.
- **Security**: Ensure compatibility with `SecurityFilterChain` bean migrations.

## Golden Snippet: Virtual Thread Controller

```java
@RestController
@RequestMapping("/api/v1")
public class AgentController {

    private final AgentService service;

    public AgentController(AgentService service) {
        this.service = service;
    }

    // Runs on virtual thread automatically in Boot 3.2+
    @PostMapping("/process")
    public ResponseEntity<Result> process(@RequestBody Task task) {
        return ResponseEntity.ok(service.execute(task));
    }
}
```
