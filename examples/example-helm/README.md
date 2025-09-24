# lob-management example

This example folder shows a hypothetical LOB repo with 1 helm application simple-service which uses a local helm chart called web-service. It's not intended to be a real/complete application but to demonstrate the principles.

The use of _environment directories at the root and within the service is the desired approach to allow configuration to be set & overridden at the appropriate points to reduce the amount of duplication present in the current lob repos branch per environment approach.

Files may exist at the configuration level thats appropriate to a given lob/service/environment & will only exist at the appropriate point, so it can't be assumed that any file would be present at a particular place.

Different files are used by different helm charts, and some files are lob/repo level whilst others are service level; so for example queue.yaml might describe the rabbit setup for the entire lob whilst service.yaml describes an individual service within the lob.

## Generating service manifests for a given environment (without CMP)

`cd examples/example-helm`

`helm dependency build simple-service`

### Simple, with defaults

`helm template simple-service`

### For a given service / environment

Simple only service config:

`helm template simple-service -f simple-service/service.yaml -f simple-service/oas.yml`

Assuming all config is duplicated in each environment so only needs to reference the correct file:

`helm template simple-service -f _environments/non-prod/local/service.yaml -f simple-service/service.yaml -f simple-service/oas.yml`

Slightly more complex:

`helm template simple-service -f _environments/non-prod/local/service.yaml -f simple-service/service.yaml -f simple-service/oas.yml -f simple-service/_environments/non-prod/local/service.yaml`

Flexibly expecting config to be supplied at an appropriate level for the use case, with a single helm command for every lob repo/service, would require the helm command to specify every possible location and every file to exist and be yaml, which isn't desirable. For example in this example this errors because one of the potential files isn't present:

`helm template simple-service -f _environments/non-prod/local/service.yaml -f _environments/non-prod/local/service.yaml -f simple-service/service.yaml -f simple-service/oas.yml -f simple-service/_environments/non-prod/service.yaml -f simple-service/_environments/non-prod/local/service.yaml`