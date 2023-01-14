
Feature: Re-Order Sortable section

  Background: Open the test page
      Given open the globalsqa "https://www.globalsqa.com" page

  Scenario Outline: Re-Order multiple_list
    Then the url is contain <page_name>
    When go to the test page
    And reorder elements <multiple_list>, <iframe_M>, <item1>, <item2>
    Then the url is contain <text>
    Then the element exist <SORTABLE2_Item1>
    Then the element exist <UL6>

    Examples:
      | SORTABLE2_Item1                             | text       | page_name      | UL6                        | iframe_M                                            | multiple_list             | item1                      | item2                      |
      | //*[@id='sortable2']/li[2][text()='Item 1'] | #Multiple  | globalsqa      | //*[@id="sortable2"]/li[6] | //*[@id="post-2675"]/div[2]/div/div/div[2]/p/iframe | //*[@id="Multiple Lists"] | //*[@id="sortable1"]/li[1] | //*[@id="sortable2"]/li[1] |


  Scenario Outline: Re-Order Portlets
    Then the url is contain <page_name>
    When go to the test page
    And reorder elements <portlets>, <iframe_P>, <el1>, <el2>
    Then the url is contain <text>
    And the element exist <FEEDS_div3>
    When click <minus>
    Then the element exist <plus>
    When click <plus>
    Then the element exist <minus>

    Examples:
      | FEEDS_div3                      | page_name   | text              | minus                                                    | plus                                                   | iframe_P                                            | portlets  | el1                 | el2                 |
      | /html/body/div[3]/div[3]/div[1] | globalsqa   | demo-site/sorting  | //*[@class="ui-icon ui-icon-minusthick portlet-toggle"] | //*[@class="ui-icon portlet-toggle ui-icon-plusthick"] | //*[@id="post-2675"]/div[2]/div/div/div[1]/p/iframe | Portlets | //*[text()="Feeds"] | //*[text()="Images"] |
