void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n){
    int i=0;
    int j=0;
    int k=0;
    if ( (m!=0) && (n!=0) ){        // case 1
        while(nums1[i] != 0){
            if (nums1[i] > nums2[j]) {
                for(k=m+j; k>i; k--){
                    nums1[k] = nums1[k-1];
                };
                nums1[i] = nums2[j];
                i++;
                j++;
            } else {
                i++;
            };
        }
        if(j<n){
            for(k=i; k<m+n; k++){
                nums1[k]=nums2[j];
                j++;
            };
        };
    }
    if ( (m==0) && (n!=0) ){        // case 2
        for (k=0; k<n; k++){
            nums1[k]=nums2[k];
        };
    };
}
/*
    if m!=0 and n!=0            case 1
        then do oringinal operation
    if m=0 and n!=0             case 2
        m=n
    if m!=0 and n=0             case 3
        do nothing
    if m=0 and n=0              case 4
        do nothing
    case 3 and case 4 can be combine into new case 3
    if n=0
        do nothing              new case 3
*/
