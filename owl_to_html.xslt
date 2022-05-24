<?xml version = "1.0" encoding = "UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:owl="http://www.w3.org/2002/07/owl#"
                xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
    <xsl:template match="/rdf:RDF">
        <html>
            <body>
                <table border="1">
                <tr>
                    <th>
                        Object Properties
                    </th>
                </tr>
                    <xsl:for-each select="owl:ObjectProperty/@rdf:about">
                        <tr>
                            <td>
                                <xsl:value-of select="substring-after(., '#')"/>
                            </td>
                        </tr>
                    </xsl:for-each>
                </table>

                <table border="1">
                 <tr>
                    <th>
                        Datatype Properties
                    </th>
                </tr>
                    <xsl:for-each select="owl:DatatypeProperty/@rdf:about">
                        <tr>
                            <td>
                                <xsl:value-of select="substring-after(., '#')"/>
                            </td>
                        </tr>
                    </xsl:for-each>
                </table>

                <table border="1">
                 <tr>
                    <th>
                        Classes
                    </th>
                </tr>
                    <xsl:for-each select="owl:Class/@rdf:about">
                        <tr>
                            <td>

                                <xsl:value-of select="substring-after(., '#')"/>
                            </td>
                        </tr>
                    </xsl:for-each>
                </table>

                <table border="1">
                 <tr>
                    <th>
                        Named Individuals
                    </th>
                </tr>
                    <xsl:for-each select="owl:NamedIndividual/@rdf:about">
                        <tr>
                            <td>
                                <xsl:value-of select="substring-after(., '#')"/>
                            </td>
                        </tr>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>