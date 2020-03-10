<?xml version="1.0" encoding="utf-8"?>
<!--

XSLT to convert CellML 1.0 to 1.1.

-->
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:mathml="http://www.w3.org/1998/Math/MathML"
    xmlns:cellml10="http://www.cellml.org/cellml/1.0#"
    exclude-result-prefixes="cellml10 mathml">

    <xsl:output method="xml" version="1.0" encoding="utf-8" indent="no"/>

    <!-- Any elements or attributes not specified below will be copied -->
    <xsl:template match="@* | node()" priority="-1.0">
        <xsl:copy>
            <xsl:apply-templates select="@* | node()"/>
        </xsl:copy>
    </xsl:template>

    <!-- CellML elements get changed to the 1.1 namespace but otherwise left the same. -->
    <xsl:template match="cellml10:*">
        <xsl:namespace name="cellml" select="http://www.cellml.org/cellml/1.1#" />
        <xsl:element name="{local-name()}" namespace="http://www.cellml.org/cellml/1.1#">
            <xsl:copy-of select="@*" />
            <xsl:apply-templates select="* | node()"/>
        </xsl:element>
    </xsl:template>

    <!-- We treat the root element specially so the cellml prefix gets declared globally in the result document -->
    <xsl:template match="cellml10:model">
        <model xmlns="http://www.cellml.org/cellml/1.1#" xmlns:cellml="http://www.cellml.org/cellml/1.1#">
            <xsl:apply-templates select="@* | node()"/>
        </model>
    </xsl:template>

    <!-- MathML gets copied over as-is -->
    <xsl:template match="mathml:*">
        <xsl:copy>
            <xsl:apply-templates select="@* | node()"/>
        </xsl:copy>
    </xsl:template>

    <!-- By default attributes on MathML elements are also copied.
        Note that the priority attribute ensures the subsequent template takes priority over this one. -->
    <xsl:template match="mathml:*/@*" priority="-0.5">
        <xsl:copy-of select="."/>
    </xsl:template>

    <!-- Except for cellml:units attributes, which need to change namespace -->
    <xsl:template match="@cellml10:units">
        <xsl:attribute name="cellml:units">
            <xsl:namespace name="cellml" select="http://www.cellml.org/cellml/1.1#" />
            <xsl:value-of select="."/>
        </xsl:attribute>
    </xsl:template>

</xsl:stylesheet>
