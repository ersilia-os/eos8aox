# Chemical Checker Signaturizer 3D

Building on the Chemical Checker bioactivity signatures (available as eos4u6p), the authors use the relation between stereoisomers and bioactivity of over 1M compounds to train stereochemically-aware signaturizers that better describe small molecule bioactivity properties. In this implementation we provide the A1, A2, A3, B1, B4 and C3 signatures

## Identifiers

* EOS model ID: `eos8aox`
* Slug: `cc-signaturizer-3d`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Representation`
* Output: `Descriptor`
* Output Type: `Float`
* Output Shape: `List`
* Interpretation: 2D projection of bioactivity signatures

## References

* [Publication](https://www.biorxiv.org/content/10.1101/2024.03.15.584974v1)
* [Source Code](https://gitlabsbnb.irbbarcelona.org/packages/signaturizer3d)
* Ersilia contributor: [GemmaTuron](https://github.com/GemmaTuron)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos8aox)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos8aox.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos8aox) (AMD64)

## Citation

If you use this model, please cite the [original authors](https://www.biorxiv.org/content/10.1101/2024.03.15.584974v1) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a MIT license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!