# CellML 1.0 Test set

Please report any issues with these tests on the [issues page](https://github.com/MichaelClerx/cellml-validation/issues).

## Valid CellML 1.0 files

The files in the `valid` subset should pass in all CellML 1.0 validators.

## Invalid CellML 1.0 files

The files in the `invalid` subset should fail in all CellML 1.0 validators.
Where possible, these files contain only a single error per file.

## Advanced number types

MathML 2 defines several number types, none of which are mentioned in the CellML 1.0 spec.
However, all examples in the spec conform to the `real` type, which is also the MathML 2 default, so in the `valid` test files we have used only `real` type numbers.
The `numbers` test set includes valid files using other number types, including the `e-notation` type which was added to MathML 2 after CellML 1.0 was published, and became one of two supported types (along with `real`) in CellML 1.1.

## Unit checking

The CellML 1.0 spec does not mention how units affect the validity of a CellML file.
Presumably, this falls under the "CellML can't stop you (entirely) from making a bad model" rule, and models containing statements such `x = 1 newton + 1 ampere` are simply bad models encoded in a valid CellML file.

For tools that do implement unit checking, the `unit_checking_consistent` set contains examples of how MathML operations from the CellML subset affect units.
The `unit_checking_inconsistent` set contains examples of unit inconsistencies.
Note that all models from both sets should validate, but software is free to complain about models from the `unit_checking_inconsistent` on other grounds.

## Unit conversion

When variables from two separate componets are connected by a `map_variables`, the CellML 1.0 spec mentions unit conversion as an optional thing software may do.
(Note that conversion _within a component_ is never mentioned, so no software is expected to deal with the case where you define x in millivolts but then give it a value in volts).
Again, it seems the units of connected variables do not affect validity of the file.

The `unit_conversion_convertible` set contains models where unit conversion between components is necessary to obtain the correct results.
The `unit_conversion_inconvertible` set contains models where connetions between varaibles with incompatible units have been made.
Note that all models from both sets should validate, but software is free to complain about models from the `unit_conversion_inconvertible` on other grounds.
None of the files in `valid` require unit conversion.

## Booleans

The CellML spec makes only confusing statements about booleans (occasionally mentioning the unit `cellml:boolean`, which cannot be assigned to any number or variables and has none of the properties of the other units).
In this test set, cases involving booleans are treated separately from unit checking conversion, as it seems likely many tools will treat booleans as a type, and e.g. implement type checking (`7 + false` is wrong) but not unit checking (`1 newton + 1 meter` is fine).
The set `booleans` contains examples of misuse of booleans.

