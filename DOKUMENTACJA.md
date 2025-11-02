## Task 1 - CI/CD Pipeline

Zaimplementowano potok CI/CD obsługujący proces automatycznego testowania, budowania i wdrażania aplikacji.  
Pipeline został skonfigurowany w GitHub Actions i obejmuje:

- instalację zależności projektowych,  
- lintowanie kodu (flake8),  
- uruchamianie testów jednostkowych (pytest),  
- skanowanie podatności (pip-audit),  
- budowę obrazów Docker,  
- publikację obrazów w GitHub Container Registry (GHCR).

Proces działa automatycznie po każdym pushu do głównej gałęzi i zapewnia pełną automatyzację wdrażania aplikacji w środowisku kontenerowym.
