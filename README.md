# Proj-4-ictv-viridic

1. Download the master species list from ICTV website: [Master Species List 2020](https://talk.ictvonline.org/files/master-species-lists/m/msl/12314)
2. Open the downloaded xlsx file and go to the third sheet
3. Save the third sheet as a csv file 
4. This csv file will be input to R for retrieval of sequences from NCBI using the rentrez package
5. Steps 2 - 4 will be completed using the pandas python script
6. Save the ICTV_VIRIDIC R script and run it to see if everything runs on your local computer or class machine
7. Next Steps: 
    - We can have the class machine run this Rscript in the background with nohup and using the & option
    - Retrieve the accession ids for all species that yield greater than 0 hits from NCBI searches
    - Retrieve the fasta sequences by doing a search with all accession ids as input
    - Parse through the fasta sequence output to only save fasta sequences that start with ">NC_" in the header
