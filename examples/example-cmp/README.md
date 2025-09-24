# lob-management cmp example

This example repo is similar to example-helm but expects the CMP to translate between the producer interface and the helm specific implementation.

Key benefits:

* Will be able to handle the fact that files are only present where they need to be
* Removes helm specific implementation details from the producer repo
    * No need to specify the name of the helm subchart in all of the config files
    * No Chart.yml
    * Removes the specification of the helm application version numbers from all of the producer lob repos services (one of the main burdens)
* We don't need additional superfluous keys (for example oas: for the oas file)
* Gives us the ability to focus on the producer structure being correct, and hide any necessary complexity in the cmp until all helm charts are updated to the new structure
