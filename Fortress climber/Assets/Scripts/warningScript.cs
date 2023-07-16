using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class warningScript : MonoBehaviour
{
    private float time = 0;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        time += Time.deltaTime;

        if (time > 0.5)
        {
            GetComponent<Renderer>().enabled = false;
        }
        if (time > 1)
        {
            GetComponent<Renderer>().enabled = true;
        }
        if (time > 2)
        {
            Destroy(gameObject);
        }
    }
}
