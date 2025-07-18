# Changelog

All notable changes to The Stack Processed v2 dataset will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2025-01-15

### Added
- Initial public release with 104,885 curated code samples
- Support for 6 programming languages (Python, JavaScript, Java, C++, Go, Rust)
- HuggingFace dataset integration with seamless loading
- Quality scoring system for code samples
- Commercial licensing with three-tier pricing structure
- Comprehensive documentation and usage examples
- Basic usage script with statistics generation
- Setup utility for easy installation

### Dataset Features
- **Total samples**: 104,885 high-quality code snippets
- **File format**: Parquet (260MB, optimized for ML workflows)
- **Languages distribution**: Balanced across 6 major programming languages
- **Quality metrics**: Each sample includes quality score (0-1)
- **Processing**: AST validation, deduplication, content filtering

### Documentation
- Complete README with usage examples
- Commercial license terms and pricing
- Installation and setup instructions
- API documentation for programmatic access
- Citation format for academic use

### Technical Specifications
- Compatible with HuggingFace `datasets` library v2.0+
- Pandas integration for data analysis
- Memory-efficient loading (streaming support)
- Cross-platform compatibility (Windows, macOS, Linux)

## [Unreleased]

### Planned Features
- Additional programming languages (TypeScript, Swift, Kotlin)
- Extended quality metrics (complexity, documentation coverage)
- Streaming API for large-scale processing
- Integration with popular ML frameworks
- Enhanced deduplication algorithms

### Known Issues
- None reported

---

## Version History

- **v2.0.0**: First commercial release (January 2025)
- **v1.x**: Internal development and testing phases

## Reporting Issues

Found a bug or have a feature request? Please use our [issue tracker](https://github.com/vinsblack/The_Stack_Processed-v2/issues).

## License Changes

- **v2.0.0**: Introduced commercial licensing model
- Previous versions were development-only (not publicly released)
