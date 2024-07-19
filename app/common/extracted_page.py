class ExtractedPage:
    """Extracted page along with metadata. Source of this page can be 
    any docment type. This is 
    """
    
    def __init__(self):
        self.content = None
        self.pageNum = None
        self.source = None
    
    def from_pdf(self, page):
        """Add a page extracted from a PDF document along with metadata
        """
        self.source = page.metadata['source']
        self.pageNum = page.metadata['page']
        self.content = page.page_content        
        
    def __str__(self):
        return self.source + " " + self.pageNum + " " + self.content        