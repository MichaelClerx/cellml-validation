# CellML 1.0 Test set

Please report any issues with these tests on the [issues page](https://github.com/MichaelClerx/cellml-validation/issues).

The table below shows the different folders in the test set, and indicates whether these files are regarded as valid or invalid.
Ambiguity in the spec regarding the validity of a folder is marked with an asterisk (*).

|= Folder                         |= Validity |
|---------------------------------|-----------|
| `valid`                         | Valid     |
| `invalid`                       | Invalid   |
|---------------------------------|-----------|
| `booleans`                      | Valid     |
| `duplicate_connections`         | Invalid*  |
| `numbers`                       | Valid*    |
| `unit_checking_consistent`      | Valid     |
| `unit_checking_inconsistent`    | Valid     |
| `unit_conversion_convertible`   | Valid     |
| `unit_conversion_inconvertible` | Valid     |
| `unit_deca`                     | Invalid   |
| `units_empty`                   | Invalid*  |

## Valid CellML 1.0 files

The files in the `valid` subset should pass in all CellML 1.0 validators.

## Invalid CellML 1.0 files

The files in the `invalid` subset should fail in all CellML 1.0 validators.
Where possible, these files contain only a single error per file.

## Booleans

The CellML 1.0 spec makes only confusing statements about booleans (occasionally mentioning the unit `cellml:boolean`, which cannot be assigned to any number or variable and has none of the other properties of a unit).
In this test set, cases involving booleans are treated separately from unit checking conversion, as it seems likely many tools will treat booleans as a type, and e.g. implement type checking (`7 + false` is wrong) but not unit checking (`1 newton + 1 meter` is fine).
The set `booleans` contains examples of misuse of booleans.
Because the spec does not state otherwise, we assume that all these files are valid CellML.

## Duplicate connections*

There is no rule in the CellML 1.0 specification that stops you from connecting the same two variables twice.
The spec does contain rules such as "a component X can only list its children in one place", suggesting that the spec was intended to be quite strict.
In CellML 2.0 it is explicitly not allowed to connect two variables twice, so in this test set we have assumed doing so is invalid.

## Advanced number types*

MathML 2 defines several number types, none of which are mentioned in the CellML 1.0 spec.
However, all examples in the spec conform to the `real` type, which is also the MathML 2 default, so in the `valid` test files we have used only `real` type numbers.
The `numbers` test set includes valid files using other number types, including the `e-notation` type which was added to MathML 2 after CellML 1.0 was published, and became one of two supported types (along with `real`) in CellML 2.0.

## Unit checking

The CellML 1.0 spec does not mention how units affect the validity of a CellML file.
Presumably, this falls under the "CellML can't stop you (entirely) from making a bad model" rule, and models containing statements like `x = 1 newton + 1 ampere` are simply bad models encoded in a valid CellML file.

For tools that do implement unit checking, the `unit_checking_consistent` set contains examples of how MathML operations from the CellML subset affect units.
The `unit_checking_inconsistent` set contains examples of unit inconsistencies.
Note that all models from both sets should validate, but software is free to complain about models from `unit_checking_inconsistent` on other grounds.

## Unit conversion

When variables from two separate components are connected by a `map_variables`, the CellML 1.0 spec mentions unit conversion as an optional thing software may do.
(Note that conversion _within a component_ is never mentioned, so no software is expected to deal with the case where you define x in millivolts but then give it a value in volts).
Again, all this is discussed in terms of software capabilities, not the CellML format, so it seems that the units of connected variables do not affect validity of the file.

The `unit_conversion_convertible` set contains models where unit conversion between components is necessary to obtain the correct results.
The `unit_conversion_inconvertible` set contains models where connections between variables with incompatible units have been made.
Note that all models from both sets should validate, but software is free to complain about models from `unit_conversion_inconvertible` on other grounds.
None of the files in `valid` should require unit conversion.

## Deka and deca

Although `deca` is the SI unit spelling, and `deka` is the youessian spelling (which is actually closer to the original greek), CellML 1.0 only allows `deka`.
However, as it allows the SI spelling for all predefined units it seems to make sense to allow `deca` too.

## Empty units elements*

The CellML spec says:

- _If a `<units>` element defines a base_units attribute with a value of "yes", then that `<units>` element must contain only the following elements, which may appear in any order:_
  - _`<RDF>` elements in the RDF namespace._
- _If a `<units> element does not define a base_units attribute with a value of "yes", then that `<units>` element must contain only the following elements, which may appear in any order:_
  - _`<unit>` elements in the CellML namespace,_
  - _`<RDF>` elements in the RDF namespace._

It is unclear from this text if a `<units>` with `base_units="no"` is required to have any `<unit>` elements.
However, (1) it is certain that `RDF` elements are not required, so presumably neither are `unit` elements, and (2) the CellML 2.0 spec explicitly allows empty `<units>` elements.

However, the spec does not say what an empty units _means_.
In CellML 2.0, an empty `<units>` element denotes a new base unit (CellML 2.0 doesn't have a `base_units` element).
For compatibility with CellML 2.0, in this set we've assumed that empty unitses are not allowed.

