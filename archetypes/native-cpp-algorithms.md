# ⚡ Archetype: Modern C++ Native Systems & Algorithms

> **Target Domain**: High-performance compute, geometric modeling, vision processing, low-level protocol engines, and native libraries with C# / Python interop.

---

## 🛠️ Technology Stack

| Layer | Technology | Rationale / Convention |
| :--- | :--- | :--- |
| **Language Standard** | Modern C++20 / C++23 | Concepts, ranges, `std::span`, `std::string_view`, `std::expected`. |
| **Build System** | MSBuild (`.vcxproj`) & CMake | Visual Studio MSBuild for Windows; CMake for cross-platform / Linux targets. |
| **Package Manager** | `vcpkg` | Manifest mode (`vcpkg.json`) for deterministic multi-platform dependencies. |
| **Memory Safety** | Strict RAII & Smart Pointers | `std::unique_ptr`, `std::shared_ptr`. Zero naked `new`/`delete` or raw owning pointers. |
| **Testing & Profiling** | GoogleTest (`gtest`) + Benchmark | Unit & simulation suites; Google Benchmark for algorithmic performance profiling. |
| **Sanitizers & Diagnostics** | ASan (`-fsanitize=address`) & UBSan | Automated memory safety and undefined behavior detection in CI. |
| **Interoperability** | `extern "C"` / `pybind11` | C-style exports for C# `[LibraryImport]` / P-Invoke; `pybind11` for Python extensions. |

---

## 📁 Directory Structure

```
MyNativeLib/
├── vcpkg.json
├── CMakeLists.txt
├── CMakePresets.json
├── README.md
├── ARCHITECTURE.md
├── include/
│   └── my_native_lib/
│       ├── api.h                 # Exported C-ABI symbols
│       ├── algorithm_engine.hpp  # High-level C++ classes
│       └── types.hpp
├── src/
│   ├── algorithm_engine.cpp
│   ├── interop_exports.cpp       # extern "C" wrappers
│   └── diagnostic_taps.cpp       # Ring buffer state dumps
└── tests/
    ├── CMakeLists.txt
    ├── test_algorithms.cpp       # GoogleTest assertions
    ├── test_harness_stress.cpp   # High-volume closed-loop simulation
    └── benchmark_algorithms.cpp  # Google Benchmark suites
```

---

## ⚙️ C-ABI Interop Pattern for C# and Python

```cpp
// include/my_native_lib/api.h
#pragma once

#if defined(_WIN32)
  #define EXPORT_API __declspec(dllexport)
#else
  #define EXPORT_API __attribute__((visibility("default")))
#endif

extern "C" {
    EXPORT_API int ProcessDataBatch(
        const double* inputData, 
        int length, 
        double* outputData, 
        char* errorBuffer, 
        int errorBufferSize
    );
}
```

```csharp
// C# .NET 9 Consumption via [LibraryImport]
using System.Runtime.InteropServices;

public static partial class NativeInterop
{
    [LibraryImport("MyNativeLib", StringMarshalling = StringMarshalling.Utf8)]
    public static partial int ProcessDataBatch(
        ReadOnlySpan<double> inputData,
        int length,
        Span<double> outputData,
        Span<byte> errorBuffer,
        int errorBufferSize
    );
}
```
