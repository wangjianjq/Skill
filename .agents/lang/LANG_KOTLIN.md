# Language: Kotlin

## Schema: Language Specification

- language: Kotlin
- category: mobile_programming_language
- latest_supported_version: 2.0+ (K2 Compiler)
- platform: Android
- ui_framework_modern: Jetpack Compose
- ui_framework_legacy: XML Views + ViewBinding
- concurrency: Coroutines + Flow (StateFlow/SharedFlow)
- architecture: MVVM + Clean Architecture

---

## [Modern] (Kotlin 2.0+, Jetpack Compose)

- **Compiler**: K2 Compiler.
- **UI**: Jetpack Compose ONLY.
- **Concurrency**: Coroutines & Flow (StateFlow/SharedFlow).

### Modern Snippet: Compose

```kotlin
@Composable
fun MainScreen() {
    val state by viewModel.uiState.collectAsStateWithLifecycle()
    Text("Modern UI")
}
```

## [Stable/Legacy] (Kotlin <1.9, XML Views)

- **UI**: XML Layouts + ViewBinding.
- **Architecture**: Fragment-based navigation.
- **Patterns**: DataBinding (legacy), `findViewById` (deprecated).
- **Concurrency**: RxJava or simple callbacks if Coroutines aren't fully integrated.

### Legacy Snippet: Fragment & ViewBinding

```kotlin
class MyFragment : Fragment(R.layout.fragment_my) {
    private val binding by viewBinding(FragmentMyBinding::bind)
}
```
