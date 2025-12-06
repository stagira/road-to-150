```mermaid
graph TD;
    A[Début] --> B{Est-ce que ça marche ?};
    B -- Oui --> C[Super !];
    B -- Non --> D[Réparer];
    D --> B;
```