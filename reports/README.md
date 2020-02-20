# Reports

The reports listed below were automatically generated during testing. Some care needs to be taken when interpreting them:

- Percentages shown are for the number of test files that were classified correctly
  - This does not necessarily correlate with the "percentage of the spec" a validation method tests
  - This certainly does not correlate with the number of errors a method will catch in the wild
- The test set includes things which the spec does not mention, but does not explicitly disallow, i.e. rational numbers or numbers with a non-decimal base in MathML
- Tools may be more strict than the spec, or choose to correct errors, for example by not allowing "123" as an identifier (valid according to the 1.0 spec)
- Tools not specifically aimed at validation will often try to be inclusive - as a *feature*

## CellML 2.0

## CellML 1.1

## CellML 1.0

- [DTD validation](dtd_1_0.md) (69%)
- [Schema validation](schema_1_0.md) (77%)
- [RelaxNG validation](relaxng_1_0.md) (81%)

External tools (tests for these are located in branches)

- [OpenCOR / CellML API](opencor_1_0.md) (88%)
- [Myokit](myokit_1_0.md) (78%)
- [Web Lab cellmlmanip](cellmlmanip_1_0.md) (39%)
